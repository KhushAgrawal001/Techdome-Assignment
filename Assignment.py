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
        driver_path = r"C:\Users\Hp\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
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

if _name_ == "_main_":
    unittest.main()