from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

award = ['打擊獎項', '投手獎項', '金手套獎', '最佳十人獎']

driver = webdriver.Chrome()
url = 'https://www.cpbl.com.tw/stats/yearaward'
driver.get(url)

wait = WebDriverWait(driver, 10)

previous_table_text = ""

for i in award:
    select_element = wait.until(EC.presence_of_element_located((By.ID, 'Award')))
    select_position = Select(select_element)
    select_position.select_by_visible_text(i)

    # click '查詢'
    search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn")))
    search_button.click()

    # wait for table to load
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

    # check table data change
    for _ in range(50):
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        table = soup.find('table')
        current_table_text = table.get_text()

        if current_table_text != previous_table_text:
            previous_table_text = current_table_text
            break
        time.sleep(0.1)

    # crawling
    df = pd.read_html(str(table))[0]
    df.to_csv(f'{i}.csv', index=False, encoding='utf-8-sig')

driver.quit()
