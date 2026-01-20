from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/118.0.5993.117 Safari/537.36"
)

service = Service(ChromeDriverManager().install())
dr = webdriver.Chrome(service=service, options=chrome_options)

dr.get("https://www.yatra.com/")

# Wait for at least one input field to appear
wait = WebDriverWait(dr, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))

print(dr.find_elements(By.TAG_NAME, "a"))
print(len(dr.find_elements(By.TAG_NAME, 'input')))

dr.quit()
