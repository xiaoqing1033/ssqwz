'''
Author: xingxing
Date: 2020-09-28 00:49:44
LastEditTime: 2020-10-30 18:18:21
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
import random
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
 lastcpid = int(x[0]) + 1
 print(lastcpid)
class DoubleBall():
    def __init__(self):
        self.db_list = []
        self.change_list(self.check_red_ball())
        self.change_list(self.check_blue_ball())
        self.print_ball()
    def check_red_ball(self):
        num_list = range(1,34)
        red_list = random.sample(num_list,6)
        red_list.sort()
        return red_list    
#生成篮球  
    def check_blue_ball(self):
        num_list = range(1,17)
        blue_list = random .sample(num_list,1)
        return blue_list
    def print_ball(self):
        print("随机一注为："+ str(self.db_list))
    def change_list(self,tem_list):
        for i in tem_list:
            self.db_list.append(i)

 if __name__ == "__main__":
     double_ball = DoubleBall()
