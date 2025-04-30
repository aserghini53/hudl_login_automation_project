# Hudl Login Automation Test Suite

This project contains automated tests for the Hudl login page using Selenium WebDriver and pytest.

## Description

This test suite verifies various functionalities of the Hudl login page, including:
- Standard login process
- Password reset flow
- Login with Google
- Account creation process
- Error handling for invalid inputs

## Installation

1. Clone the repository:

git clone https://github.com/aserghini53/hudl-login-tests.git
cd hudl-login-tests

2. Set up a virtual environment (optional but recommended):
    
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate


3. Install the required packages:
    
pip install -r requirements.txt


## Configuration

1. Update the CONSTANT.py file under test_data with the following content:
   USER_EMAIL = your_test_username
   USER_PASSWORD = your_test_password


## Usage

To run the tests in the terminal using the following command:

pytest --html=report.html --self-contained-html

To run a specific file in the terminal using the following command:

pytest tests/test_login.py --html=report.html --self-contained-html

To run a specific method in a class in the terminal using the following command:

pytest tests/test_login.py::TestLogin::test_valid_login --html=report.html --self-contained-html


## Project Structure

- `locators/`: Contains all locator elements
- `tests/`: Contains all test files
- `pages/`: Page Object Model classes
- `tests_data/`: Contains all test data
- `conftest.py`: pytest fixtures and configurations
- `requirements.txt`: List of project dependencies

## Key Features

- Automated login tests
- Password reset flow verification
- Google SSO testing
- Cross-browser testing capability
- Page Object Model design pattern

## Dependencies

- Selenium WebDriver
- pytest
- Python 3.x
