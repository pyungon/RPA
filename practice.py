from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

url = "https://naver.com"

driver.get(url)
time.sleep(3) # 사람이 입력한 것처럼 보이도록 시간 주기

# 1
# query = driver.find_element(By.ID, "query")
# # query = driver.find_element(By.NAME, "query") : 위 코드와 같은 의미
# query.send_keys("인공지능")
# time.sleep(2)

# search_btn = driver.find_element(By.CSS_SELECTOR, "#search-btn")
# search_btn.click()
# time.sleep(2)

# 2
driver.find_element(By.ID, "query").send_keys("인공지능")
time.sleep(2)

# driver.find_element(By.CSS_SELECTOR, "#search-btn").click()
driver.find_element(By.ID, "query").send_keys(Keys.ENTER)
time.sleep(2)

driver.save_screenshot("naver_인공지능.png")

driver.quit()
