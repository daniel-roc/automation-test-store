# Automation Test Store Project

This is a training test automation project of the website [Automation Test Store](https://www.automationteststore.com/), a place to practice your automation skills.

The technologies used are Python (version 3.10.6) with venv, Pytest and Selenium Webdriver.

## Project Structure

The project is structured with two main folders:

- **tests**: This folder contains the test scripts that use Pytest framework and Selenium Webdriver to interact with the web elements and verify the expected results.
- **page_object**: This folder contains the page object classes that represent each web page of the Automation Test Store website. Each class has methods to locate and manipulate the web elements on that page.

## Prerequisites

To run this project, you need to have **Google Chrome** browser installed on your machine, as it is the default browser used by the test scripts.

If you encounter compatibility issues between the Selenium WebDriver and the version of Google Chrome installed on your computer, it's recommended to update the Selenium package to ensure compatibility. To update the Selenium package inside the project, you can use the following command:

`pip install --upgrade selenium`

Running this command will update the Selenium package to the latest version available, which should help resolve any compatibility problems with your Google Chrome browser. Make sure you run this command within your project's virtual environment (activated as described in the installation instructions) to ensure that the package is updated specifically for your project.

## Installation

To check this repository and install the dependencies in your own machine, follow these steps:

1. Clone this repository using `git clone https://github.com/daniel-roc/automation-test-store.git`
2. Create a virtual environment using `python -m venv venv`
3. Activate the virtual environment using `venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux/Mac
4. Install the required packages using `pip install -r requirements.txt`

## Running the Tests

To run the tests in the terminal, use the following commands:

- On Windows: `py.test tests --html=reports\report.html`
- On Linux/Mac: `python -m pytest tests --html=reports/report.html`

This will generate an HTML report with the test results in the current directory.

## Author

This project was created by **Daniel Rocha**. You can connect with me on [Linkedin](https://www.linkedin.com/in/danielrocha25/).