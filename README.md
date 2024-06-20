# E-Commerce Website Testing Project

## Introduction
This project involves manual and automated testing of an eCommerce website, focusing on the entire process from logging in to making a payment for a product. The project includes a detailed manual test case and an automated test script using Selenium WebDriver with Python.

## Table of Contents
- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Manual Test Case](#manual-test-case)
- [Automated Test Script](#automated-test-script)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Notes](#notes)
- [Contact Information](#contact-information)

## Project Structure
```
ecommerce-testing-project/
│
├── README.md
├── requirements.txt
├── test_login.py
└── report/
    └── TestReport.html
```

## Manual Test Case
### Objective
Verify the complete process from logging into an eCommerce website to successfully making a payment for a product.

### Test Steps
1. Navigate to the website and verify homepage loads.
2. Login using valid credentials.
3. Search for a product (e.g., "laptop").
4. Select a product from the search results.
5. Add the product to the cart.
6. Proceed to checkout.
7. Enter shipping information.
8. Select payment method and enter details.
9. Review and place order.
10. Verify order confirmation and email receipt.

### Expected Results
- User should be able to log in successfully.
- Product search should return relevant results.
- The product should be added to the cart and the order should be successfully placed.

## Automated Test Script
The automated test script uses Selenium WebDriver with Python to automate the login process of an eCommerce website.

### test_login.py
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest

class ECommerceLoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'
        driver_path = r"C:\path\to\chromedriver.exe"
        chrome_service = Service(driver_path)
        chrome_options = Options()
        chrome_options.add_argument(f'user-agent={user_agent}')
        cls.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    def setUp(self):
        self.driver.get("https://www.allbirds.com/account")
        self.close_popup()

    def close_popup(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            popup_close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "jsx-4037854530.IconButton.Modal__close")))
            popup_close_button.click()
        except TimeoutException:
            print("No popup appeared or couldn't find the close button.")

    def test_login(self):
        wait = WebDriverWait(self.driver, 10)

        email_field = wait.until(EC.presence_of_element_located((By.ID, "CustomerEmail")))
        email_field.send_keys("test.vic3456@gmail.com")

        password_field = self.driver.find_element(By.ID, "CustomerPassword")
        password_field.send_keys("Test@@1234")

        login_button = self.driver.find_element(By.CLASS_NAME, "btn.btn--full")
        login_button.click()

        welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Welcome')]")))
        self.assertIn("Welcome", welcome_message.text)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
```

## Prerequisites
- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Unittest

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/khushagrawal001/Techdome-Assignment.git
   cd Techdome-Assignment
   ```

2. Install required packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Download and install ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/).

## Usage
1. **Manual Testing**: Follow the steps outlined in the manual test case section to test the login to payment process manually.

2. **Automated Testing**:
   - Open `test_login.py`.
   - Update the `driver_path` variable with the path to your ChromeDriver executable.
   - Run the script:
     ```sh
     python test_login.py
     ```

3. **Generate Report**:
   - The report is generated using `HTMLTestRunner`.
   - The generated report will be available in the `report` directory as `TestReport.html`.

## Notes
- The provided script focuses on the login functionality. It will need to be adjusted according to the specific structure and elements of the target website.
- This is a basic implementation. In a production environment, additional considerations such as error handling, logging, and comprehensive validation checks would be implemented.

## Contact Information
- **LinkedIn**: [TechDome Solutions](https://www.linkedin.com/company/techdome-solutions)
- **Website**: [techdome.net.in](https://techdome.net.in)
- **Email**: [contact@techdome.net.in](mailto:contact@techdome.net.in)
- **Phone**: +91-7723849516, +91-9826073971
- **Address**: A/75, Vidhya Palace Colony, Aerodrum Road, Indore (M.P.), 452009

Thank you for reviewing this project. Please feel free to contact us for any further information or clarification.
