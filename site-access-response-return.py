import requests

url = 'https://vacation-stay.jp/listings/192716'
response = requests.get(url)

# サーバからの応答のステータスコードが200（成功）ならば、HTMLを表示
if response.status_code == 200:
    print(response.status_code)	
#    print(response.text)
else:
    print('Error: ' + str(response.status_code))
