from requests import get
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import time
import os
import csv 
 
def request_content(start, end):
    url_link = 'https://datachart.500.com/ssq/history/newinc/history.php?start={0}&end={1}'.format(start, end)
    headers = {
        'User-Agent': generate_user_agent(device_type='desktop', os=('mac', 'linux', 'win', 'android'))
    }
    response = get(url_link, headers=headers, timeout=6)
    page_content = BeautifulSoup(response.content, "html.parser")
    html_tag = page_content.find_all('tbody', id='tdata')[0]
    return html_tag.find_all('tr', 't_tr1')
def write_data(data, name):
    with open(name, 'w', errors='ignore', newline='') as f:
        csvFile = csv.writer(f)
        csvFile.writerows(data) 
 
class ssqclazz:
    def __init__(self):
        self.period = ''  # 期号
        self.red_1 = ''  # 红球
        self.red_2 = ''
        self.red_3 = ''
        self.red_4 = ''
        self.red_5 = ''
        self.red_6 = ''
        self.blue_1 = ''  # 蓝球
        self.lottery_kjhm = ''  # kaijiang号码
        self.pool_prize = ''  # 奖池奖金(元)
        self.first_count = ''  # 一等奖 注数
        self.first_prize = ''  # 一等奖 奖金(元)
        self.second_count = ''  # 二等奖 注数
        self.second_prize = ''  # 二等奖 奖金(元)
        self.total_prize = ''  # 总投注额(元)
        self.lottery_date = ''  # 开奖日期
 
    def __str__(self):
        return '{0}，{1}，{2}，{3}，{4}，{5}，{6}，{7}，{8}，{9}，{10}，{11}，{12}，{13}，{14}，{15}'.format(self.period, self.red_1,
                                                                                              self.red_2, self.red_3,
                                                                                              self.red_4, self.red_5,
                                                                                              self.red_6,
                                                                                              self.blue_1,
                                                                                              self.lottery_kjhm,
                                                                                              self.pool_prize,
                                                                                              self.first_count,
                                                                                              self.first_prize,
                                                                                              self.second_count,
                                                                                              self.second_prize,
                                                                                              self.total_prize,
                                                                                              self.lottery_date)
 
    def tr_tag(self, tag):
        tds = tag.find_all('td')
        index = 0
        self.period = tds[index].string
        index += 1
        self.red_1 = tds[index].string
        index += 1
        self.red_2 = tds[index].string
        index += 1
        self.red_3 = tds[index].string
        index += 1
        self.red_4 = tds[index].string
        index += 1
        self.red_5 = tds[index].string
        index += 1
        self.red_6 = tds[index].string
        index += 1
        self.blue_1 = tds[index].string
        index += 1  #快乐是空值
        self.lottery_kjhm = f'{self.red_1} {self.red_2} {self.red_3} {self.red_4} {self.red_5} {self.red_6} {self.blue_1}'
        index += 1
        self.pool_prize = tds[index].string
        index += 1
        self.first_count = tds[index].string
        index += 1
        self.first_prize = tds[index].string
        index += 1
        self.second_count = tds[index].string
        index += 1
        self.second_prize = tds[index].string
        index += 1
        self.total_prize = tds[index].string
        index += 1
        self.lottery_date = tds[index].string
 

if __name__ == '__main__':
    filename = "ssq.txt"
    if  os.path.exists(filename):
        print("更新")
        os.remove(filename)
        os.remove("12.csv")
    file = open('ssq.txt', mode='a+', encoding='utf-8')
    localtime = time.localtime(time.time())
    lyear = localtime.tm_year
    ymin = 3  # 双色球03年上线
    ymax = lyear - 2000
    print('===抓取数据开始===，200%s-20%s' % (ymin, ymax))
    list = []
    for year in range(ymin, ymax + 1):
        start = '{0}001'.format(year)
        end = '{0}300'.format(year)
        trs = request_content(start, end)
        for tr in trs:
            ssqobj = ssqclazz()
            ssqobj.tr_tag(tr)
            objstr = ssqobj.__str__()
            list.append(objstr)
            file.write(objstr)
            file.write('\n')
            print(objstr)
        file.write('\n')
        print()
        time.sleep(3)
    file.close()
    write_data(list,'12.csv')
    print('抓取完毕！！！')