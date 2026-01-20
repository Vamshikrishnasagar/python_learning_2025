from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import time
from selenium.webdriver.chrome.options import Options




class YatraNoLogin:
    def yatra_web_page(self):
        dr = None
        try:
            service = Service(ChromeDriverManager().install())
            chrome_options = Options()
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
            time.sleep(2)
            text1 = dr.find_element(By.CSS_SELECTOR, "div[title='Up to Rs. 2,025 OFF'] span[class='MuiTypography-root MuiTypography-body1 css-1aj3ppi']").text
            print(text1)
            time.sleep(2)

        except Exception as e:
            print(e)
        finally:
            if dr:
                dr.quit()



person01 = YatraNoLogin()
person01.yatra_web_page()