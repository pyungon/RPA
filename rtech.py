from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import urllib.request
import time
import os
BACKSPACE='/ue003'
ENTER='/ue007'
TAB='/ue004'



options = Options()
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)
# 자동화 메세지 옵션 제거
options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=options)

url = "https://rtech.or.kr/main/mapSearch.do?posX="

driver.get(url)
time.sleep(3)  


# login_text_element = driver.find_element(By.CLASS_NAME, "color-red")
# login_text = login_text_element.text
# print(login_text)
# driver.find_element("id", "txtExstPrlno").send_keys(login_text)
# time.sleep(3)
# driver.find_element("id", "txtExstPrlno").send_keys(Keys.ENTER)
# time.sleep(3)

# 관할자치단체
select = Select(driver.find_element(By.NAME, 'do_code1'))
select.select_by_index(1)
time.sleep(2)

select_1 = Select(driver.find_element(By.NAME, 'city_code1'))
select_1.select_by_index(1)
time.sleep(2)

select_2 = Select(driver.find_element(By.NAME, 'dong_code1'))
select_2.select_by_index(1)
time.sleep(2)


driver.find_element("id", "searchInput").send_keys("상봉동 동부아파트")
time.sleep(3)
# driver.find_element("id", "txtExstPrlno").send_keys(Keys.ENTER)s
# time.sleep(3)
driver.find_element(By.ID, "quickSearchResult").click()
time.sleep(3)

driver.find_element(By.ID, "map_pop_info_bottom_btn").click()
time.sleep(3)

