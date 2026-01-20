from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


class YatraNoLogin:
    def yatra_web_page(self):
        dr = None
        try:
            service = Service(ChromeDriverManager().install())


            chrome_options = Options()
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-geolocation")
            chrome_options.add_argument("--disable-infobars")
            chrome_options.add_argument("--log-level=3")
            chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


            dr = webdriver.Chrome(service=service, options=chrome_options)

            dr.get("https://www.yatra.com/")
            print(dr.title)
            dr.maximize_window()

            # Wait for at least one input field to appear
            wait = WebDriverWait(dr, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Login']")))

            try:
                wait.until(EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "span[class='style_cross__q1ZoV'] img[alt='cross']"))).click()
            except:
                print("No pop-up appeared.")

            time.sleep(5)

            # alerts = dr.switch_to.alert
            # if alerts:
            #     alerts.accept()
            # dr.switch_to.alert.send_keys("Hello")
            # dr.switch_to.alert.accept()


            text1 = dr.find_element(By.CSS_SELECTOR, "div[title='Up to Rs. 2,025 OFF'] span[class='MuiTypography-root MuiTypography-body1 css-1aj3ppi']").text
            print(text1)
            time.sleep(2)

            # departure_from = dr.find_element(By.ID, "input-with-icon-adornment-label")
            # departure_from.click()
            # time.sleep(2)
            # departure_from.send_keys("New Delhi")
            # time.sleep(2)
            # departure_from.send_keys(Keys.ENTER)
            # time.sleep(2)

            # Calender
            # dr.find_element(By.CSS_SELECTOR, ".css-13lub7m").click()
            # time.sleep(2)


            # Multiple Windows:
            parent_window = dr.current_window_handle
            print(parent_window)

            dr.find_element(By.XPATH, "//span[@type='travel-agent']").click()
            all_handles = dr.window_handles
            print(len(all_handles))
            for handle in all_handles:
                if handle != parent_window:
                    dr.switch_to.window(handle)
                    time.sleep(2)
                    email_id = "testing123@gmail.com"
                    for char in email_id:
                        dr.find_element(By.XPATH, "//input[@id='email']").send_keys(char)
                        # time.sleep(0.3)
                        dr.find_element(By.XPATH, "//button[@type='submit']").click()
                    time.sleep(2)
                    dr.close()
                    time.sleep(2)
                    break

            dr.switch_to.window(parent_window)
            time.sleep(2)
            dr.find_element(By.XPATH, "//p[normalize-space()='Support']//span").click()
            time.sleep(2)


        except Exception as e:
            print(e)
        finally:
            if dr:
                dr.quit()

 
person01 = YatraNoLogin()
person01.yatra_web_page()