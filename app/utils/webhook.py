import hmac
import hashlib
import functools
import os
from flask import request
from app.exceptions import WebhookSignatureException

SUPPORTED_ALGORITHMS = {
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
    "sha1": hashlib.sha1,
}

def validate_webhook_signature(
    header: str = "X-Hub-Signature-256",
    algorithm: str = "sha256",
    prefix: str = "sha256=",
):
    """
    Decorator to validate webhook HMAC signature.

    Args:
        header:     The request header containing the signature.
        algorithm:  Hashing algorithm to use (sha256, sha512, sha1).
        prefix:     Prefix to strip from the header value before comparing.

    Usage:
        @ns.route("/")
        class WebhookResource(Resource):
            @validate_webhook_signature()
            def post(self):
                ...
    """
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            _validate(header, algorithm, prefix)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def _validate(header: str, algorithm: str, prefix: str):
    """Internal function to perform the actual signature validation."""
    if algorithm not in SUPPORTED_ALGORITHMS:
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Choose from: {list(SUPPORTED_ALGORITHMS)}")

    signature_header = request.headers.get(header)

    if not signature_header:
        raise WebhookSignatureException(f"Missing signature header: {header}")

    raw_body = request.get_data()

    received_signature = (
        signature_header.removeprefix(prefix)
        if prefix
        else signature_header
    )

    secret_key = os.getenv("WEBHOOK_SECRET_KEY")

    expected_signature = hmac.new(
        secret_key.encode(),
        raw_body,
        SUPPORTED_ALGORITHMS[algorithm],
    ).hexdigest()

    if not hmac.compare_digest(expected_signature, received_signature):
        raise WebhookSignatureException("Invalid webhook signature")