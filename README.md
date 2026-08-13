# QA Automation Framework

UI test automation framework built with Python, Selenium WebDriver and pytest using the Page Object Model.

## Test Application

SauceDemo is used to demonstrate and practice automated UI testing scenarios such as authentication, product management, shopping cart functionality and the complete checkout flow.

Application: https://www.saucedemo.com/

## Tech Stack

- Python
- Selenium WebDriver
- pytest

## Design Pattern

- Page Object Model

## Features

- Page Object architecture
- Cross-browser testing
- Chrome and Firefox support
- Headless mode
- Environment selection
- pytest fixtures
- Test parametrization
- Smoke, regression and negative markers
- Explicit waits
- Logging to console and files
- Automatic screenshots on test failure
- Alerts and iFrames support
- Multiple windows and tabs
- ActionChains
- Select dropdowns
- Shopping cart interactions
- End-to-end checkout flow

## Project Structure

```text
QA_Automation_Framework/
├── config/
├── data/
├── locators/
├── logs/
├── pages/
├── screenshots/
├── tests/
├── utils/
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md 
```
## Test Coverage

The current test suite covers:

- Successful and invalid login scenarios
- Product addition and removal from the shopping cart
- Shopping cart state validation
- End-to-end checkout flow
- Checkout page transitions and successful order completion
- Browser interactions including alerts, iFrames, multiple tabs, hover actions and dropdowns

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

Run all tests:

```bash
pytest
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

Run tests in Firefox:

```bash
pytest --browser=firefox
```

Run tests on the production environment:

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

Logs are stored in:

```text
logs/
```

Screenshots for failed UI tests are stored in:

```text
screenshots/
```

Both directories are generated automatically.


## Architecture

The framework uses the Page Object Model.

Common Selenium actions are implemented in `BasePage`.

Test setup and dependencies are managed through pytest fixtures.

Browser creation is isolated in `browser_factory.py`.

Configuration is separated from test data.

Logging and screenshot utilities are stored in `utils/`.