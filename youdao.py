import requests
import json
word = input('请输入要翻译的内容：')
url = 'http://fanyi.youdao.com/translate'
data = {'i': word,'doctype': 'json'}   
headers = {'User-Agent': 'Mozilla/5.0'}       
response = requests.post(url,data=data,headers=headers)
html=response.content.decode('utf-8')
result = json.loads(html)['translateResult'][0][0]['tgt']
print(result)