# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     service = Service("D:\\WebDrivers\\Chrome_WebDriver\\chromedriver.exe")
#     driver = webdriver.Chrome(service=service)
#
#     driver.get("https://www.tcs.com")
#     print(driver.title)
#     driver.maximize_window()
#     driver.save_screenshot("D:\\PythonProjects\\Python_Learning_Youtube_2025\\TestFile.png")
#     time.sleep(5)
#     driver.quit()
# except Exception as e:
#     print(e)




import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
# Automatically download & use correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.tcs.com")
time.sleep(3)
print(driver.title)
driver.maximize_window()



driver.sleep(3)
driver.save_screenshot("D:\\PythonProjects\\Python_Learning_Youtube_2025\\SeleniumWithPython\\TestFile12.png")
driver.minimize_window()
driver.maximize_window()
driver.back()
time.sleep(1)
driver.quit()




"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

try:
    service = Service("D:\\WebDrivers\\MS_Edge_WebDriver\\msedgedriver.exe")
    # driver = webdriver.Chrome(service=service)
    driver = webdriver.Edge(service=service)

    driver.get("https://www.tcs.com")
    print(driver.title)
    driver.maximize_window()
    driver.save_screenshot("D:\\PythonProjects\\Python_Learning\\TestFile11.png")
    time.sleep(5)
    driver.quit()
except Exception as e:
    print(e)
"""
