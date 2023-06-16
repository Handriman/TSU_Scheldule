import requests
import execjs

url = 'https://tulsu.ru/schedule/script.js?v=1686857243'
response = requests.get(url)
js_code = response.text

context = execjs.compile(js_code)
table_data = context.call("AddLessons;")
