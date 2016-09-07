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
games=['fallout3','L4D2']
ran_games={"fallout3":random(),"L4D2":random()}
if ran_games["fallout3"]>ran_games["L4D2"]:
    prize1="fallout3"
    prize2="L4D2"
else:
    prize2="fallout3"
    prize1="L4D2"
for idx,key in  enumerate(ran):
    if  idx==0:
        print("随机数：{0:<25} 肥宅：{1:<25}Prize:{2:<25}".format(key,list[key].strip(),prize1).strip())
        text=(("随机数：{0:<25} 肥宅：{1:<25}Prize:{2:<25}".format(key,list[key].strip(),prize1).strip())+"\n").encode("utf-8")
        result.write(text)
    elif    idx==1:
        print("随机数：{0:<25} 肥宅：{1:<25}Prize:{2:<25}".format(key,list[key].strip(),prize2).strip())
        text=(("随机数：{0:<25} 肥宅：{1:<25}Prize:{2:<25}".format(key,list[key].strip(),prize2).strip())+"\n").encode("utf-8")
        result.write(text)
    elif idx>1:
        print("随机数：{0:<25} 肥宅：{1:<25}".format(key,list[key]).strip())
        text=(("随机数：{0:<25} 肥宅：{1:<25}".format(key,list[key]).strip())+"\n").encode("utf-8")
        result.write(text)

result.close()
