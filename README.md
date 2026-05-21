# SauceDemo Test Automation

This is a simple test automation setup for [SauceDemo](https://www.saucedemo.com). It's built with Python, Pytest, and Selenium, and uses the Page Object Model (POM) pattern.

## Project Structure
- `pages/`: Contains the Page Object Models for the different screens (login, cart, checkout, etc).
- `tests/`: Contains the actual test files.

## How to run the tests

First, set up a virtual environment and install the dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To run all the tests at once:
```bash
pytest
```

To view the test report (this project uses Allure for reporting):
```bash
allure serve allure-results
```

## Running specific tests

If you just want to run a specific test file, you can point pytest straight to it:

```bash
# E2E checkout flow
pytest tests/test_e2e.py

# Cart functionality
pytest tests/test_cart.py

# Login functionality
pytest tests/test_login.py
```

If you need to run a single specific test case, you can do it like this:
```bash
pytest tests/test_login.py::TestLogin::test_invalid_login
```

## Running in slow motion (visual mode)

By default, the tests run headlessly so they finish as fast as possible. If you're debugging or just want to watch the tests execute in an actual browser window:

1. Open `conftest.py` and comment out the `--headless` flag.
2. Open `pages/base_page.py` and make sure `import time` is at the top of the file.
3. Add `time.sleep(1)` to the bottom of the `click` and `type_text` functions inside `base_page.py`.
4. Run `pytest` again. 

The browser will now pop up and you'll see the test pause for a second after every click or typing action.
