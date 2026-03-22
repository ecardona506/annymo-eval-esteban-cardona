# REST API - Technical Test Kit - Block 1

REST API created as a solution to the first block of the technical test kit. This project implements a user management system with secure user creation and retrieval endpoints.

## Project Description

This is a Flask-based REST API designed for user management operations. It provides endpoints for creating new users and listing existing users with pagination support. The API includes features such as:

- User registration with password hashing
- User data validation before creation
- Webhook signature validation for secure user creation
- Paginated user listing
- Comprehensive error handling and logging
- Database migrations using Flask-migrate
- Docker containerization support for both the application and the database

## Requirements

- Docker

### Dependencies

The project uses the following main dependencies:

- **Flask** (>= 3.1.3): Web framework
- **Flask-SQLAlchemy** (>= 3.1.1): Database ORM
- **Flask-RESTX** (>= 1.3.2): API documentation and validation
- **Flask-Bcrypt** (>= 1.0.1): Password hashing
- **Flask-Migrate** (>= 4.1.0): Database migrations
- **Flask-Marshmallow** (>= 1.4.0): Object serialization
- **psycopg2-binary** (>= 2.9.11): PostgreSQL adapter
- **pytest** (>= 9.0.2): Testing framework

## Installation


1. **Clone the repository**

   ```
   git clone https://github.com/ecardona506/annymo-eval-esteban-cardona.git
   ```

2. **Set up environment variables**:
   Create a `.env` file. This file should follow the `.env.example` structure

## Usage

### Running the Application

#### Start the app
```bash
docker-compose up --build -d
```

#### Stop the app
```bash
docker-compose down
```

The API will be accessible at `http://localhost:5000`.

### API Endpoints

#### Create User
- **Endpoint**: `POST /api/v1/users/create`
- **Description**: Creates a new user
- **Headers**:
  - `X-Hub-Signature-256`: HMAC signature for webhook validation (required). I suggest use [this tool](https://cryptotools.net/hmac) to generate the HMAC signature using the payload of the request and the WEBHOOK_SECRET_KEY.

- **Request Body**:
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "phone_number": "+1234567890",
    "password": "securepassword"
  }
  ```
- **Response**: User object with ID

#### List Users
- **Endpoint**: `GET /api/v1/users/all`
- **Description**: Retrieves a paginated list of users
- **Query Parameters**:
  - `page` (optional): Page number (default: 1)
  - `per_page` (optional): Items per page (default: 10)
- **Response**:
  ```json
  {
    "users": [
      {
        "id": "1",
        "name": "John Doe",
        "email": "john@example.com",
        "phone_number": "+1234567890"
      }
    ],
    "pagination": {
      "page": 1,
      "per_page": 10,
      "total": 1,
      "pages": 1
    }
  }
  ```

## Project Structure

```
annymo-eval-esteban-cardona/
├── app/                         # Main application package
│   ├── __init__.py              # Flask app factory
│   ├── api/                     # API modules
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── routes/          # API route definitions
│   │       │   ├── __init__.py
│   │       │   └── user.py      # User-related endpoints
│   │       └── schemas/         # API schema definitions
│   │           ├── __init__.py
│   │           └── user.py      # User data schemas for serialization
│   ├── config.py                # Configuration classes
│   ├── extensions.py            # Flask extensions
│   ├── exceptions/              # Custom exceptions
│   │   ├── __init__.py
│   │   ├── base.py              # Base exception class
│   │   ├── handler.py           # Error handlers
│   │   ├── user.py              # User-related exceptions
│   │   └── webhook.py           # Webhook-related exceptions
│   ├── models/                  # Database models
│   │   ├── __init__.py
│   │   └── user.py              # User model
│   ├── services/                # Business logic services
│   │   ├── __init__.py
│   │   └── user.py              # User service
│   └── utils/                   # Utility functions
│       └── webhook.py           # Webhook utilities
├── migrations/                  # Database migrations (Alembic)
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions/                # Migration scripts
├── instance/                    # Instance-specific data
├── main.py                      # Application entry point
├── pyproject.toml               # Project configuration and dependencies
├── Dockerfile                   # Docker image definition
├── docker-compose.yaml          # Docker Compose configuration
├── entrypoint.sh                # Docker entrypoint script
└── README.md                    # This file
```

### Key Components

- **API Layer** (`app/api/`): Handles HTTP requests and responses using Flask-RESTX
- **Services Layer** (`app/services/`): Contains business logic and database operations
- **Models Layer** (`app/models/`): PostgreSQL database models
- **Exceptions** (`app/exceptions/`): Custom exception classes and error handling
- **Configuration** (`app/config.py`): Environment-specific settings
- **Utilities** (`app/utils/`): Helper functions like webhook validation

This structure follows a clean architecture pattern, separating concerns between API, business logic, and data layers.