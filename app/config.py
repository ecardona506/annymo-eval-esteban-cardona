import os

# Flask configuration classes for different environments
class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv("SECRET_KEY", "my_secret_key")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True  # Ensure exceptions propagate to error handlers

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

# Dict mapping environment names to config classes
config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}