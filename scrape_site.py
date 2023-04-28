import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def scrape_site(url):
    # 取得済みのページを保存するセット
    scraped_urls = set()
    
    # 再帰的にページをスクレイピングする関数
    def recursive_scrape(url):
        # 取得済みの場合はスキップ
        if url in scraped_urls:
            return
        
        # 拡張子が除外対象の場合はスキップ
        excluded_exts = ('.jpg', '.pdf')
        if any(url.endswith(ext) for ext in excluded_exts):
            return
        
        # ページを取得
        response = requests.get(url)
        scraped_urls.add(url)
        
        # HTMLをパースしてリンクを取得
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        
        # 同じドメインのリンクを取得して再帰的にスクレイピング
        for link in links:
            href = link.get('href')
            if href is not None:
                parsed_href = urlparse(href)
                if parsed_href.netloc == domain and parsed_href.scheme in ('http', 'https'):
                    next_url = href if bool(parsed_href.netloc) else f'{domain}/{href}'
                    recursive_scrape(next_url)
    
    # ドメインを取得
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    
    # 再帰的にスクレイピング
    recursive_scrape(url)
    
    # 取得済みのページのURLを返す
    return "\n".join(sorted(scraped_urls, key=len))

scraped_urls = scrape_site('https://enta.proudit.jp')
print(scraped_urls)
