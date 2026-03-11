from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd

team = ['ADD', 'ACN', 'AJL', 'AEO', 'AAA', 'AKP', 'AJK']
name = ['統一獅', '中信兄弟', '樂天桃猿', '富邦悍將', '味全龍', '台鋼雄鷹', 'Lamigo']
year = ['2025', '2024', '2023', '2022', '2021', '2020', '2019', '2018', '2017']
year = year[::-1]
data = ['打擊成績', '投球成績', '守備成績']

# team
for i in range(len(team)):
    driver = webdriver.Chrome()
    url = f'https://www.cpbl.com.tw/team/teamscore?ClubNo={team[i]}'
    driver.get(url)
    try:
        # year
        for j in year:
            select = Select(driver.find_element(By.NAME, "Year"))
            select.select_by_visible_text(f'{j}年')
            
            # data
            for k in data:
                WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.ID, 'Position'))
                )
                dropdown = driver.find_element(By.ID, 'Position')
                select_position = Select(dropdown)
                select_position.select_by_visible_text(f'{k}')
                
                # wait for click
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "btn"))
                )
                
                # click '查詢'
                search_button = driver.find_element(By.CLASS_NAME, "btn")
                search_button.click()
                
                # wait for table
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'table'))
                )

                # crawling
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                table = soup.find('table')
                
                # table exist or not
                if table:
                    df = pd.read_html(str(table))[0]
                    df.to_csv(f'{j}_{name[i]}_{k}.csv', index=False, encoding='utf-8-sig')
                
    except Exception as e:
        print(f"{name[i]}, error: {e}")
    finally:
        driver.quit()
