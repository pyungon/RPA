from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import os

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?h1=ko&ogb1")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("Mercedes" + Keys.ENTER)

# Scroll Down
elem = driver.find_element(By.TAG_NAME, 'body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

# View More
try:
    view_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'mye4qd')))
    view_more_button.click()
    for i in range(80):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass

# images = driver.find_elements(By.CSS_SELECTOR, "YQ4gaf")
# links = [image.get_attribute('src') for image in images if image.get_attribute('src') is not None]
# print('찾은 이미지의 개수 : ', len(links))

# 이미지 추출
images = driver.find_elements(By.TAG_NAME, "img")
links = [image.get_attribute('src') for image in images if image.get_attribute('src') or image.get_attribute('data-src')]

# 추출한 이미지 링크 개수 출력
print('찾은 이미지의 개수 : ', len(links))

# 저장할 폴더 경로
save_path = 'C:/Users/shciojt/Desktop/이성원/img_download/'

# 폴더가 없으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 이미지 다운로드
for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, os.path.join(save_path, str(k) + '.jpg'))