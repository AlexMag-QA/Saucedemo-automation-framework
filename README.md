# QA Automation Framework

Automation testing framework built with Python, Selenium WebDriver, pytest, Requests, Pydantic, PostgreSQL and Psycopg.

The project demonstrates UI, REST API and Database test automation using a layered framework architecture, Page Object Model, API Client pattern, Repository pattern, pytest fixtures, schema validation and isolated database transactions.

## Test Applications

### UI Testing

SauceDemo is used for automated UI testing scenarios including authentication, product management, shopping cart functionality and the complete checkout flow.

Application: https://www.saucedemo.com/

### API Testing

JSONPlaceholder is used for REST API testing, including CRUD operations, query parameters, negative scenarios and response schema validation.

API: https://jsonplaceholder.typicode.com/

DummyJSON is used for authentication scenarios including login, Bearer token authentication and protected endpoints.

API: https://dummyjson.com/

### Database Testing

PostgreSQL is used for database testing scenarios.

Database tests cover data validation, positive and negative scenarios, parametrized queries, data modification and transaction rollback.

Test data modifications are automatically rolled back after tests to keep database tests isolated.

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- Requests
- Pydantic
- PostgreSQL
- Psycopg
- python-dotenv
- REST API
- Page Object Model
- API Client pattern
- Repository pattern

## Features

### UI Automation

- Page Object Model architecture
- Chrome and Firefox support
- Headless mode
- Environment selection
- pytest fixtures
- Test parametrization
- Smoke, regression and negative markers
- Explicit waits
- Logging to console and files
- Automatic screenshots on test failure
- Alerts and iFrames
- Multiple windows and tabs
- ActionChains
- Select dropdowns
- Shopping cart interactions
- End-to-end checkout flow

### API Automation

- GET, POST, PUT, PATCH and DELETE requests
- API Client architecture
- `requests.Session`
- Centralized API configuration
- Request headers and query parameters
- JSON request and response validation
- Bearer token authentication
- Positive and negative API scenarios
- pytest parametrization
- Pydantic schema validation
- Strict response type validation
- CRUD testing

### Database Automation

- PostgreSQL database testing
- Psycopg database connection
- Parameterized SQL queries
- Positive and negative database scenarios
- pytest fixtures
- pytest parametrization
- Dictionary-based query results
- INSERT and UPDATE testing
- Automatic transaction rollback
- Test data isolation
- Repository pattern
- Centralized database operations
- Environment-based database configuration
- Secrets excluded from Git

## Project Structure

```text
QA_Automation_Framework/
├── api/
│   ├── __init__.py
│   └── posts_client.py
│
├── config/
│   └── api_settings.py
│
├── database/
│   ├── __init__.py
│   └── users_repository.py
│
├── data/
│
├── locators/
│
├── models/
│   ├── __init__.py
│   └── post_model.py
│
├── pages/
│
├── tests/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_negative_posts.py
│   │   ├── test_posts.py
│   │   └── test_query_params.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   └── test_users_db.py
│   │
│   └── UI tests
│
├── utils/
│
├── logs/
│
├── screenshots/
│
├── .env.example
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Architecture

The framework separates test scenarios from technical implementation.

### UI Layer

```text
Tests
  ↓
Page Objects
  ↓
BasePage
  ↓
Selenium WebDriver
  ↓
Web Application
```

Common Selenium actions are implemented in `BasePage`.

Browser creation is isolated in `browser_factory.py`.

pytest fixtures manage browser setup, teardown and test dependencies.

Page Objects contain page-specific actions and hide Selenium implementation from tests.

### API Layer

```text
Tests
  ↓
API Client
  ↓
requests.Session
  ↓
REST API
  ↓
Pydantic Models
  ↓
Assertions
```

API endpoints are stored in configuration.

`PostsClient` contains HTTP request logic and uses `requests.Session`.

Pydantic models validate API response structure and data types.

Tests contain test scenarios and assertions without duplicating HTTP implementation.

### Database Layer

```text
Tests
  ↓
UsersRepository
  ↓
Psycopg Cursor
  ↓
PostgreSQL
```

Database tests do not contain duplicated SQL implementation.

`UsersRepository` contains SQL operations related to users and provides reusable methods such as:

```python
get_user_by_id()
create_user()
update_user_age()
```

pytest fixtures manage database connections and cursors.

Database-changing tests are isolated using transaction rollback:

```text
SETUP
  ↓
Database Connection
  ↓
Cursor
  ↓
Test
  ↓
ROLLBACK
  ↓
Connection Cleanup
```

This allows tests to create or modify database records without permanently changing test data.

Database credentials are loaded from environment variables and are not stored in source code.

## Test Coverage

### UI

The UI test suite covers:

- Successful and invalid login
- Product addition and removal from the shopping cart
- Shopping cart state validation
- End-to-end checkout
- Browser alerts
- iFrames
- Multiple tabs
- Hover actions
- Dropdowns

### API

The API test suite covers:

- Authentication
- Bearer token usage
- Missing and invalid tokens
- CRUD operations
- Query parameter filtering
- Positive and negative scenarios
- Parametrized API tests
- Response headers
- Pydantic schema validation
- Strict data type validation

### Database

The database test suite covers:

- Existing user validation
- Nonexistent user validation
- Parametrized database tests
- SELECT queries
- INSERT operations
- UPDATE operations
- Database result validation
- Positive and negative database scenarios
- Transaction rollback
- Test data isolation
- Repository-based database access

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move to the project directory:

```bash
cd QA_Automation_Framework
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Database Configuration

Database credentials are stored in environment variables.

Create a local `.env` file in the project root using `.env.example` as a template:

```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=qa_training
DB_USER=postgres
DB_PASSWORD=your_password
```

The real `.env` file is excluded from Git.

Do not store real database passwords in `.env.example` or source code.

PostgreSQL must be available before running database tests.

## Running Tests

Run the complete test suite:

```bash
pytest -v
```

Run only UI tests:

```bash
pytest tests -v --ignore=tests/api --ignore=tests/db
```

Run only API tests:

```bash
pytest tests/api -v
```

Run only Database tests:

```bash
pytest tests/db -v
```

Run smoke tests:

```bash
pytest -m smoke
```

Run regression tests:

```bash
pytest -m regression
```

Run tests in headless mode:

```bash
pytest --headless
```

Run UI tests in Firefox:

```bash
pytest --browser=firefox
```

Run tests for the production environment:

```bash
pytest --env=prod
```

Options can be combined:

```bash
pytest -m smoke --browser=chrome --env=prod --headless
```

## CLI Options

| Option | Description |
|---|---|
| `--env` | Select test environment |
| `--browser` | Select Chrome or Firefox |
| `--headless` | Run browser without visible UI |

## Pytest Markers

- `smoke` — critical application functionality
- `regression` — regression test suite
- `negative` — negative scenarios

## Test Artifacts

Logs are generated in:

```text
logs/
```

Screenshots for failed UI tests are generated in:

```text
screenshots/
```

Generated test artifacts are excluded from Git.

## Dependencies

Main project dependencies:

```text
selenium==4.45.0
pytest==9.1.1
requests==2.34.2
pydantic==2.13.4
psycopg==3.3.4
psycopg-binary==3.3.4
python-dotenv==1.2.3
```

## Current Status

The framework currently contains automated:

- UI tests
- REST API tests
- Database tests

The project uses three automation layers:

```text
UI
Tests → Page Objects → Selenium

API
Tests → API Client → Requests

Database
Tests → Repository → Psycopg → PostgreSQL
```

Latest full regression run:

```text
45 passed
```

Current framework capabilities include UI automation, API testing, schema validation, database testing, transaction isolation, logging, screenshots and multi-browser execution.

The project is continuously extended as new automation testing technologies and framework components are added.