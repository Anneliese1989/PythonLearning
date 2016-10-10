import  re
import  os
import  random
from    io  import  *
from    collections import  *
from    random  import  random
import urllib.request   
with urllib.request.urlopen('https://docs.python.org/3.5/howto/regex.html') as f:

    data=str(f.read())
    print(data)
    p=re.compile('href="[\S]+"')
    p2=re.compile('src="[\S]+"')   
    m=p.findall(data)
    n=p2.findall(data)
    result2=open("A.txt","wb")
    result2=open("A.txt","ab")
    result2.write(data.encode("utf-8"))
    result2.close()

    result=open("B.txt","wb")
    result=open("B.txt","ab")

    if  m:
        for x   in  m:
            print("found: "+x+"\n")
            result.write((x+"\n").encode("utf-8"))
    else:
        print("not found")
        
    if  n:
        for x   in  n:
            print("found: "+x+"\n")
            result.write((x+"\n").encode("utf-8"))
    else:
        print("not found")

    result.close()

     