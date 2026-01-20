import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.yatra.com/support")
driver.maximize_window()
time.sleep(2)
print(driver.title)
support_button = driver.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
more_button = driver.find_element(By.XPATH, "//a[@class='dropdown-toggle eventTrackable']")


mouse =  ActionChains(driver)
mouse.move_to_element(support_button).perform()
time.sleep(2)
mouse.click(more_button).perform()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@class='simple-tab eventTrackable adobeTracking'][normalize-space()='Make a Payment']").click()
time.sleep(2)
driver.quit()