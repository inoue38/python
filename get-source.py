from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# WebDriverのパスを設定
webdriver_service = Service(ChromeDriverManager().install())

# ヘッドレスモードを設定
chrome_options = Options()
chrome_options.add_argument("--headless")

# WebDriverを使用してブラウザを起動（ヘッドレスモード）
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# 指定したURLにアクセス
driver.get('https://vacation-stay.jp/search?adults=2&destination=%E6%9D%B1%E4%BA%AC&page=2&sort=distance_asc')

# ページが完全にロードされるまで待つ
driver.implicitly_wait(10)

# ページのソースを取得
source = driver.page_source

print(source)

# ブラウザを閉じる
driver.quit()

