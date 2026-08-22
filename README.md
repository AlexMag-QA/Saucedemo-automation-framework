# QA Automation Framework

Automation testing framework built with Python, Selenium WebDriver, pytest, Requests and Pydantic.

The project demonstrates UI and REST API test automation using a layered framework architecture, Page Object Model, API Client pattern, pytest fixtures and schema validation.

## Test Applications

### UI Testing

SauceDemo is used for automated UI testing scenarios including authentication, product management, shopping cart functionality and the complete checkout flow.

Application: https://www.saucedemo.com/

### API Testing

JSONPlaceholder is used for REST API testing, including CRUD operations, query parameters, negative scenarios and response schema validation.

API: https://jsonplaceholder.typicode.com/

DummyJSON is used for authentication scenarios including login, Bearer token authentication and protected endpoints.

API: https://dummyjson.com/

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- Requests
- Pydantic
- REST API
- Page Object Model
- API Client pattern

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

## Project Structure

```text
QA_Automation_Framework/
├── api/
│   └── posts_client.py
├── config/
│   └── api_settings.py
├── data/
├── locators/
├── models/
│   └── post_model.py
├── pages/
├── tests/
│   ├── api/
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_negative_posts.py
│   │   ├── test_posts.py
│   │   └── test_query_params.py
│   └── UI tests
├── utils/
├── logs/
├── screenshots/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Architecture

The framework separates test logic from technical implementation.

### UI Layer

```text
Tests
  ↓
Page Objects
  ↓
BasePage
  ↓
Selenium WebDriver
```

Common Selenium actions are implemented in `BasePage`.

Browser creation is isolated in `browser_factory.py`.

pytest fixtures manage browser setup and test dependencies.

### API Layer

```text
Config
  ↓
API Client
  ↓
requests.Session
  ↓
REST API
  ↓
Pydantic Models
  ↓
Tests / Assertions
```

API endpoints are stored in configuration.

`PostsClient` contains HTTP request logic and uses `requests.Session`.

Pydantic models validate API response structure and data types.

Tests contain test scenarios and assertions without duplicating HTTP implementation.

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

## Installation

Clone the repository:

```bash
git clone <repository-url>
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

## Running Tests

Run the complete test suite:

```bash
pytest -v
```

Run only API tests:

```bash
pytest tests/api -v
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

Generated artifacts are excluded from Git.

## Current Status

The framework currently contains automated UI and REST API tests.

Latest full regression run:

```text
39 passed
```

The project is continuously extended as new automation testing technologies and framework components are added.