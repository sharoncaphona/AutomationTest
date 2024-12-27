import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class TestJobApplicationForm(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-popup-blocking")
        service = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/automation-practice-form")
        self.test_log = open("test_log.txt", "a")  # Log file

    def test_valid_form_submission(self):
        try:
            driver = self.driver
            driver.find_element(By.ID, "firstName").send_keys("Sam")
            driver.find_element(By.ID, "lastName").send_keys("Shane")
            driver.find_element(By.ID, "userEmail").send_keys("sam@gmail.com")
            gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
            gender_male.click()
            driver.find_element(By.ID, "userNumber").send_keys("1234567890")
            submit_btn = driver.find_element(By.ID, "submit")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            submit_btn.click()
            confirmation_msg = driver.find_element(By.ID, "example-modal-sizes-title-lg").text
            self.assertEqual(confirmation_msg, "Thanks for submitting the form")
            self.test_log.write("PASS: test_valid_form_submission\n")
        except Exception as e:
            self.test_log.write(f"FAIL: test_valid_form_submission - {str(e)}\n")

    def test_email_field_blank(self):
        try:
            driver = self.driver
            driver.find_element(By.ID, "firstName").send_keys("Sam")
            driver.find_element(By.ID, "lastName").send_keys("Shane")
            driver.find_element(By.ID, "userEmail").send_keys("")
            gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
            gender_male.click()
            driver.find_element(By.ID, "userNumber").send_keys("1234567890")
            submit_btn = driver.find_element(By.ID, "submit")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            submit_btn.click()
            error_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Email is required')]").text
            self.assertIn("Email is required", error_msg)
            self.test_log.write("PASS: test_email_field_blank\n")
        except Exception as e:
            self.test_log.write(f"FAIL: test_email_field_blank - {str(e)}\n")

    def test_future_date_of_birth(self):
        try:
            driver = self.driver
            driver.find_element(By.ID, "firstName").send_keys("Sam")
            driver.find_element(By.ID, "lastName").send_keys("Shane")
            driver.find_element(By.ID, "userEmail").send_keys("sam@gmail.com")
            gender_male = driver.find_element(By.XPATH, "//label[text()='Male']")
            driver.execute_script("arguments[0].scrollIntoView(true);", gender_male)
            gender_male.click()
            driver.find_element(By.ID, "dateOfBirthInput").send_keys("12/28/2025")
            driver.find_element(By.ID, "userNumber").send_keys("1234567890")
            submit_btn = driver.find_element(By.ID, "submit")
            driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
            submit_btn.click()
            error_msg = driver.find_element(By.XPATH, "//div[contains(text(),'Invalid Date of Birth')]").text
            self.assertIn("Invalid Date of Birth", error_msg)
            self.test_log.write("PASS: test_future_date_of_birth\n")
        except Exception as e:
            self.test_log.write(f"FAIL: test_future_date_of_birth - {str(e)}\n")

    def tearDown(self):
        self.driver.quit()
        self.test_log.close()

if __name__ == "__main__":
    unittest.main()
