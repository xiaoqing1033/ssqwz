'''
Author: xingxing
Date: 2020-09-28 00:49:44
LastEditTime: 2020-10-31 01:25:12
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \pythontext\ssqmysql.py
'''

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import mysql.connector
from requests import get
from bs4 import BeautifulSoup
from user_agent import generate_user_agent
import time
import os
#数据库链接

mydb = mysql.connector.connect(
host="localhost",
user="satest",
passwd="123456",
database="datefenxi"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT max(cpid)  FROM ssqcq_his ")
myresult = mycursor.fetchall()
for x in myresult:
    lastcpid = x[0] 
    print(lastcpid)
mydb.close() 
 #数据下载
def request_content(start, end):
    url_link = 'https://datachart.500.com/ssq/history/newinc/history.php?start={0}&end={1}'.format(start, end)
    headers = {
        'User-Agent': generate_user_agent(device_type='desktop', os=('mac', 'linux', 'win', 'android'))
    }
    response = get(url_link, headers=headers, timeout=6)
    page_content = BeautifulSoup(response.content, "html.parser")
    html_tag = page_content.find_all('tbody', id='tdata')[0]
    return html_tag.find_all('tr', 't_tr1')

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
       # self.happy_sunday = ''  # 快乐星期天
        self.pool_prize = ''  # 奖池奖金(元)
        self.first_count = ''  # 一等奖 注数
        self.first_prize = ''  # 一等奖 奖金(元)
        self.second_count = ''  # 二等奖 注数
        self.second_prize = ''  # 二等奖 奖金(元)
        self.total_prize = ''  # 总投注额(元)
        self.lottery_date = ''  # 开奖日期
        self.lottery_kjhm = '' #开奖号码
        
 
    def __str__(self):
        return '{0}，{1}，{2}，{3}，{4}，{5}，{6}，{7}，{8}，{9}，{10}，{11}，{12}，{13}，{14}，{15}'.format(self.period, self.red_1,
                                                                                              self.red_2, self.red_3,
                                                                                              self.red_4, self.red_5,
                                                                                              self.red_6,
                                                                                              self.blue_1,
                                                                                             # self.happy_sunday,
                                                                                              self.pool_prize,
                                                                                              self.first_count,
                                                                                              self.first_prize,
                                                                                              self.second_count,
                                                                                              self.second_prize,
                                                                                              self.total_prize,
                                                                                              self.lottery_date,
                                                                                              self.lottery_kjhm)
 
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
        index += 1
        #self.happy_sunday = tds[index].string
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
        self.lottery_kjhm = f'{self.red_1} {self.red_2} {self.red_3} {self.red_4} {self.red_5} {self.red_6} {self.blue_1}'
 
if __name__ == '__main__':
    filename = "ssq.txt"
    if  os.path.exists(filename):
        print("更新")
        os.remove(filename)
    file = open(filename, mode='a+', encoding='utf-8')
    localtime = time.localtime(time.time())
    lyear = localtime.tm_year
    ymin = 20  # 双色球03年上线
    ymax = lyear - 2000
    print('===抓取数据开始===，200%s-20%s' % (ymin, ymax))
    #打开数据库连接，指定数据库
    conn = mysql.connector.connect(
    host="localhost",
    user="satest",
    passwd="123456",
    database="datefenxi"
    )
    cur = conn.cursor()#获取游标
    '''
    sql = "INSERT INTO  ssqcq_his  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        %(ssqobj.period,ssqobj.lottery_date,ssqobj.red_1,ssqobj.red_2,ssqobj.red_3,ssqobj.red_4
        ,ssqobj.red_5,ssqobj.red_6,ssqobj.blue_1,ssqobj.lottery_kjhm,ssqobj.first_count,
        ssqobj.first_prize, ssqobj.pool_prize)
        '''
    list=[]
    for year in range(ymin, ymax + 1):
        #start = '{0}001'.format(year)
        start = lastcpid + 1  
        end = '{0}300'.format(year)
        print(start)
        print(end)
        trs = request_content(start, end)
        for tr in trs:
            ssqobj = ssqclazz()
            ssqobj.tr_tag(tr)
            objstr = ssqobj.__str__()
            #list.append()#//
            file.write(objstr)
            file.write('\n')
            print(objstr)
            
        file.write('\n')
        print(list)
        print()
        time.sleep(3)
        
        #try:
        #另一种插入数据的方式，通过字符串传入值
        #有问题
        '''
        row_count = cur.execute(sql,())
        print ('批量插入返回受影响的行数：%d',row_count)
        cur.close()
        conn.commit()
        conn.close()
        print("sql执行成功)
        except:
            # 发生错误时回滚
            db.rollback()
            '''
    file.close()
    print('抓取完毕！！！')    
 




