import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

# WebDriverのパスを設定
webdriver_service = Service(ChromeDriverManager().install())

# ヘッドレスモードを設定
chrome_options = Options()
chrome_options.add_argument("--headless")

# WebDriverを使用してブラウザを起動（ヘッドレスモード）
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 指定したURLにアクセス
driver.get('https://vacation-stay.jp/search?adults=2&destination=%E6%9D%B1%E4%BA%AC&sort=distance_asc')

# ページが完全にロードされるまで待つ
driver.implicitly_wait(10)

# ページのソースを取得
source = driver.page_source
# print(source)

# ブラウザを閉じる
# driver.quit()

# # BeautifulSoupオブジェクトを作成
soup = BeautifulSoup(source, 'html.parser')
# print(soup)

#最終ページを取得
aria_label_pattern = re.compile('.*')  # 任意の文字列を持つaria-label属性を検索するための正規表現パターン
elements = soup.find_all('a', {'aria-label': aria_label_pattern})
last_page = int(elements[-1].text)

# for element in elements:
#     print(element)

for i in range(1, last_page + 1):
# for i in range(1, 5):
    # print(i)
    # print(f'https://vacation-stay.jp/search?adults=2&destination=%E6%9D%B1%E4%BA%AC&page={i}&sort=distance_asc')

    # WebDriverを使用してブラウザを起動（ヘッドレスモード）
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

    # 指定したURLにアクセス
    driver.get(f'https://vacation-stay.jp/search?adults=2&destination=%E6%9D%B1%E4%BA%AC&page={i}&sort=distance_asc')

    # ページが完全にロードされるまで待つ
    driver.implicitly_wait(10)

    # ページのソースを取得
    source = driver.page_source
    # print(source)

    # ブラウザを閉じる
    # driver.quit()

    # # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(source, 'html.parser')



# pattern = re.compile('notranslate app-javascript-packs-search-index-___listing_item__property-title___*')
# elements = soup.find_all('p', class_=pattern)

#価格を取得
# elements = soup.find_all('span', class_='app-javascript-packs-search-index-___listing_item__price-unit___fWJDq')

# prices = []
# for element in elements:
#     next_sibling = element.next_sibling
#     if next_sibling and next_sibling.string:
#         prices.append(next_sibling.string.strip())

# print(prices)


# pattern = re.compile('notranslate app-javascript-packs-search-index-___listing_item__property-title|app-javascript-packs-search-index-___listing_item__price-range___7LChk')
# elements = soup.find_all(['p', 'span'], class_=pattern)

# for element in elements:
#     print(element.text)

# pattern = re.compile('notranslate app-javascript-packs-search-index-___listing_item__property-title|app-javascript-packs-search-index-___listing_item__price-range___7LChk')
    pattern = re.compile('notranslate app-javascript-packs-search-index-___listing_item__property-title|app-javascript-packs-search-index-___listing_item__price-range')
    elements = soup.find_all(['p', 'span'], class_=pattern)

    for index, element in enumerate(elements, start=1):  # インデックスは1から開始
        # print(element.text, end='')  # 改行を抑制
        if index % 2 == 0:  # インデックスが偶数の場合
            print(element.text, end=',\n')  # カンマと改行を挿入
        else:
            print(element.text, end=', ')  # カンマを挿入


# # # 指定したクラスを持つ要素を抽出
# # elements = soup.find_all('p' ,class_='notranslate app-javascript-packs-search-index-___listing_item__property-title___2Fqz7')
# print(elements)




# # # 要素のテキストを取得
# element_texts = [element.text for element in elements]
# print(element_texts)

# # # CSVファイルに保存
# # with open('elements.csv', 'w', newline='', encoding='utf-8') as f:
# #     writer = csv.writer(f)
# #     for text in element_texts:
# #         writer.writerow([text])