from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time


class Yatra:
    def __init__(self):
        # Create a folder to store screenshots
        self.screenshot_folder = "Screenshots"
        if not os.path.exists(self.screenshot_folder):
            os.makedirs(self.screenshot_folder)

    def save_screenshot(self, driver, filename):
        # Save screenshot inside the folder
        path = os.path.join(self.screenshot_folder, filename)
        driver.save_screenshot(path)
        print(f"Screenshot saved at: {path}")

    def user_login(self, mobile_number):
        dr = None
        try:
            service = Service(ChromeDriverManager().install())
            dr = webdriver.Chrome(service=service)
            dr.get('https://www.yatra.com/')
            time.sleep(2)
            print(dr.title)
            dr.maximize_window()

            # Take initial screenshot
            self.save_screenshot(dr, "Yatra.png")

            # Enter mobile number digit by digit
            for digit in mobile_number:
                dr.find_element(By.XPATH, "//input[@id='mobile-number']").send_keys(digit)
                time.sleep(0.3)

            dr.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
            print("Please enter OTP manually on the website. Waiting 30 seconds...")
            time.sleep(30)

            dr.find_element(By.XPATH, "//button[normalize-space()='Verify']").click()
            time.sleep(5)

            # Take screenshot after login
            self.save_screenshot(dr, "User_Logged.png")
            dr.find_element(By.CSS_SELECTOR, "button[id='simple-tab-4'] span:nth-child(1)").click()
            time.sleep(5)
            self.save_screenshot(dr, "Train.png")
            time.sleep(2)


        except Exception as error:
            print("Error:", error)

        finally:
            if dr:
                dr.quit()


if __name__ == "__main__":
    testing1 = Yatra()
    mobile_number = input("Please enter your mobile number: ")
    testing1.user_login(mobile_number=mobile_number)
