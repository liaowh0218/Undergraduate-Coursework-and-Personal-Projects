from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

team = ['ADD', 'ACN', 'AJL', 'AEO', 'AAA', 'AKP']
name = ['統一獅', '中信兄弟', '樂天桃猿', '富邦悍將', '味全龍', '台鋼雄鷹']
for i in range(6):
    driver = webdriver.Chrome()
    url = f'https://www.cpbl.com.tw/team/teamrecord?ClubNo={team[i]}'
    driver.get(url)

    # crawling
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')
    df = pd.read_html(str(table))[0]
    df.to_csv(f'{name[i]} 球隊戰績.csv', index=False, encoding='utf-8-sig')

    driver.quit()
