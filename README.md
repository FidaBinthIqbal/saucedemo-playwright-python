# SauceDemo Playwright Automation

![Playwright
Tests](https://github.com/FidaBinthIqbal/saucedemo-playwright-python/actions/workflows/tests.yml/badge.svg)

End-to-end UI test automation for the
[SauceDemo](https://www.saucedemo.com/) web application using **Python,
Playwright, and Pytest**.

The project follows the **Page Object Model (POM)** to keep page
interactions separate from test assertions and uses **GitHub Actions**
to run the test suite automatically on every push and pull request.

## Tech Stack

-   **Python 3.12**
-   **Playwright**
-   **Pytest**
-   **pytest-playwright**
-   **Page Object Model (POM)**
-   **Git / GitHub**
-   **GitHub Actions**
-   **Chromium**

## Project Structure

``` text
saucedemo-playwright-python/
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── order_complete_page.py
│
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── test_cases.md
└── README.md
```

## What Is Tested

### Login

-   Login with valid credentials
-   Invalid password
-   Locked-out user
-   Empty username and password
-   Empty password

### Products & Cart

-   Add a single product
-   Add multiple products
-   Remove a product
-   Verify cart contents
-   Verify product information
-   Remove all products
-   Continue shopping

### Checkout

-   Complete checkout with valid information
-   Missing required information
-   Cancel checkout
-   Order completion
-   Whitespace-only checkout information

### Logout

-   Successful logout and return to the login page

## Test Design

The project uses the **Page Object Model**.

Page objects contain:

-   Locators
-   Page interactions
-   Reusable page-level methods

Test files contain:

-   Test scenarios
-   Assertions
-   Test data
-   Expected behavior

For example:

``` python
products_page.add_product_to_cart("Sauce Labs Backpack")
products_page.open_cart()

cart_page.checkout()
```

This keeps the tests readable while allowing page interactions to be
reused.

## Running the Tests Locally

### 1. Clone the repository

``` bash
git clone https://github.com/FidaBinthIqbal/saucedemo-playwright-python.git
cd saucedemo-playwright-python
```

### 2. Create a virtual environment

``` bash
python3 -m venv .venv
```

Activate it on macOS/Linux:

``` bash
source .venv/bin/activate
```

### 3. Install dependencies

``` bash
python -m pip install -r requirements.txt
```

### 4. Install Playwright browsers

``` bash
python -m playwright install chromium
```

### 5. Run the test suite

``` bash
pytest
```

## Running Specific Test Files

Run login tests:

``` bash
pytest tests/test_login.py
```

Run cart tests:

``` bash
pytest tests/test_cart.py
```

Run checkout tests:

``` bash
pytest tests/test_checkout.py
```

Run with the Chromium browser explicitly:

``` bash
pytest --browser chromium
```

## Failure Evidence

The project is configured to capture useful Playwright debugging
evidence when tests fail:

-   Screenshots on failure
-   Playwright traces on failure

The relevant configuration is in `pytest.ini`.

A trace can be opened with:

``` bash
playwright show-trace test-results/<test-folder>/trace.zip
```

The generated `test-results/` directory is excluded from Git using
`.gitignore`.

## CI/CD with GitHub Actions

The project uses GitHub Actions to automatically:

1.  Check out the repository
2.  Set up Python
3.  Install project dependencies
4.  Install Chromium
5.  Run the Pytest suite

Workflow file:

``` text
.github/workflows/tests.yml
```

The workflow runs on:

-   Pushes to `main`
-   Pull requests targeting `main`

This provides a basic CI pipeline for the automated tests.

## Current Test Result

The current CI suite collects **19 tests**.

Current expected result:

``` text
18 passed
1 skipped
0 failed
```

The skipped test is a documented known application issue rather than a
test failure.

## Known Issue

### BUG-001 --- Checkout accepts whitespace-only customer information

**Scenario:** TC14

**Steps:**

1.  Log in with valid credentials.
2.  Add `Sauce Labs Backpack` to the cart.
3.  Open checkout.
4.  Enter spaces in First Name, Last Name, and Postal Code.
5.  Click Continue.

**Expected Result:**

The application should reject whitespace-only values and display a
validation error.

**Actual Result:**

The application accepts the whitespace-only values and proceeds to the
Checkout Overview page.

**Status:** Observed

The corresponding automated test is skipped in CI so that the known
application defect does not hide the status of the rest of the
regression suite.

## QA Practices Demonstrated

This project demonstrates practical QA automation concepts including:

-   Functional UI testing
-   Positive and negative testing
-   Boundary/edge-case testing
-   Assertions
-   Locator strategies
-   Page Object Model
-   Test fixtures
-   Test parametrization
-   Test isolation
-   Failure screenshots
-   Playwright tracing
-   Git version control
-   CI test execution with GitHub Actions
-   Defect documentation

## Future Improvements

Potential extensions to the project include:

-   HTML test reporting
-   Uploading test reports as GitHub Actions artifacts
-   More data-driven test scenarios
-   Cross-browser execution
-   Parallel test execution
-   API + UI integration testing
-   Docker-based test execution

## Author

**Fida Binth Iqbal**

QA Engineer / Test Automation Learner

GitHub: [FidaBinthIqbal](https://github.com/FidaBinthIqbal)
