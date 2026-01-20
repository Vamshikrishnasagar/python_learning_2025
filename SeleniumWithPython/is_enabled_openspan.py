from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class openspan_app:
    def checking(self, username, pwd):
        dr = None
        try:
            service = Service(ChromeDriverManager().install())
            dr = webdriver.Chrome(service=service)

            dr.get("https://training.openspan.com/login")
            print(dr.title)
            dr.maximize_window()
            time.sleep(2)

            enabled = dr.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
            print(f"Before Entering the values, the sign button is: {enabled}")

            for i in username:
                dr.find_element(By.ID, "user_name").send_keys(i)
                time.sleep(0.3)
            for j in pwd:
                dr.find_element(By.XPATH, "//input[@id='user_pass']").send_keys(j)
                time.sleep(0.3)
            time.sleep(3)

            enabled_1 = dr.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
            print(f"Before Entering the values, the sign button is: {enabled_1}")
            dr.find_element(By.XPATH, "//input[@id='login_button']").click()
            time.sleep(3)

            # Selecting the dropdown menu
            dropdown = dr.find_element(By.ID, "productType").click()
            time.sleep(2)
            dropdown = dr.find_element(By.ID, "productType").click()
            time.sleep(2)

            dd = Select(dr.find_element(By.ID, "productType"))
            dd.select_by_index(1)
            time.sleep(2)
            dd.select_by_visible_text("Seasonings")
            time.sleep(2)



        except Exception as error:
            print(error)

        finally:
            if dr:
                dr.quit()


test_case1 = openspan_app()
test_case1.checking(
    username=input("Enter your username: "),
    pwd=input("Enter your password: "),
)
