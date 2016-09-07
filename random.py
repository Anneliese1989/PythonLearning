# Created Date : 2016-9-6 22:10
# Author       : Anneliese
#
# Description  : gift give away
#

import  os
import  random
from    io  import  *
from    collections import  *
from    random  import  random

file=open("paticipators.txt",encoding="utf-8")
list={}
for x in file.readlines():
    if  ''== x.strip():
        continue
    list[random()]=x

ran=[]
for index in  list:
    ran+=[index]
ran.sort()
ran.reverse()
result=open("result.txt","wb")
result=open("result.txt","ab")
for index in  ran:
    print("随机数：{0:<25} 肥宅：{1:<20}".format(index,list[index]).strip())
    text=(("随机数：{0:<25} 肥宅：{1:<20}".format(index,list[index]).strip())+"\n").encode("utf-8")
    result.write(text)
result.close()
