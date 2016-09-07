import io
from io import open

result=open("test.txt","wb")
result.write("this is a line".encode("utf-8"))
result.close()