#coding:utf-8
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

input_file = open("hp.txt","r")
string = input_file.read()

reg = '哈利波特与.+[ ]+:[ ]+第[0-9]{1,2}章'
patt = re.compile(reg,re.I)
res_list = re.findall(patt,string)

print len(res_list)
for res in res_list:
  print res