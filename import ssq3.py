import requests
import csv
import socket
import urllib.request as req
import urllib
from bs4 import BeautifulSoup
import gzip
import ssl
import httplib2
 
# 获取双色球往期数据
# @author puck
# @Date 2018-02-01
# https://datachart.500.com/ssq/history/history.shtml
# https://datachart.500.com/ssq/history/newinc/history.php?limit=30&sort=0
 
def get_content(url):
    try:
        context = ssl._create_unverified_context()
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        # requset = req.Request(url, headers=headers, method='GET')
        # result = req.urlopen(requset, timeout=10, context=context).read() # 此方法获取的内容貌似16进制乱码
        # rep.encoding = 'utf-8'
        # return rep.text
        # print(type(result))
        # print(result.decode())
 
        ## Available
        # h = httplib2.Http('.cache')
        # resp, content = h.request(url)
        # print(content.decode())
        # return content.decode()
 
        ## Available
        resp = requests.get(url, headers=headers, timeout=10, verify=False) # verify 参数必传，falst不校验SSL证书
        contents = resp.content
        # print(type(contents))
        # print(contents)
        if contents:
            return contents.decode()
        else:
            print("can't get data from url:" + url)
    except req.HTTPError as e:
        print('HTTPError:', e)
    except req.URLError as e:
        # SSL证书验证失败错误
        # URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (_ssl.c:748)>
        print('URLError:', e)
    except socket.timeout as e:
        print('socket.timeout:', e)
    except BaseException as e:
        print('BaseException:', e)
 
def get_data(html):
    if html is None:
        return
    final = []
    bs = BeautifulSoup(html, "html.parser")
    print(bs)
    datas = bs.find("tbody", {'id': 'tdata'})
    trs = datas.find_all('tr')
    for tr in trs:
        temp = []
        tds = tr.find_all('td')
        temp.append(tds[0].string)
        temp.append(tds[1].string)
        temp.append(tds[2].string)
        temp.append(tds[3].string)
        temp.append(tds[4].string)
        temp.append(tds[5].string)
        temp.append(tds[6].string)
        temp.append(tds[7].string)
        final.append(temp)
    print(final)
    return final
 
def write_data(data, name):
    with open(name, 'w', errors='ignore', newline='') as f:
        csvFile = csv.writer(f)
        csvFile.writerows(data)
 
if  __name__  == '__main__':
    url = 'https://datachart.500.com/ssq/history/newinc/history.php?limit=30&sort=0'
    html = get_content(url)
    data = get_data(html)
    write_data(data, 'TwoColorBallData30.csv')