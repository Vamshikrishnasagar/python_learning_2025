from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def check_box_sugarcrm():
    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.sugarcrm.com/au/request-demo/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
        driver.find_element(By.CSS_SELECTOR, "label[for='input_1_12_1']").click()
        time.sleep(2)


    except Exception as error:
        print(error)

    finally:
        if driver:
            driver.quit()

check_box_sugarcrm()