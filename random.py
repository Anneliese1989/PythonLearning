# Created Date 2016-9-6 22:10
# Random 

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
for index in  ran:
    print("随机数：{0:<20} 肥宅：{1:<20}".format(index,list[index]))

    #void* data -- 'data' is a pointer to data of unknown type, and cannot be dereferenced