
import time
import os
import uuid

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

filename = 'shot'
link = 'https://google.com'


options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--headless')
options.add_argument('--start-maximized')
driver = webdriver.Chrome(options=options)
try:
    driver.get(link)
    time.sleep(3)
    ele = driver.find_element(By.TAG_NAME, 'body')
    '''
    Кстати говоря, таким же способом можно делать скриншоты определенных
     элементов (просто находим нужный элемент и записываем в переменную ele)
    '''
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(1920, height)
    if not os.path.exists("screenshots"):
        os.mkdir("screenshots")

    # Генерируем уникальное имя файла
    unique_filename = str(uuid.uuid4())
    driver.save_screenshot(f"screenshots/{filename}-{unique_filename}.jpg")

except Exception:
    pass

finally:
    driver.close()
    driver.quit()


