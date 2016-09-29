
array=[1,5,3,2,5,7,8,9,0,5,2,4,6,78,3,54,6,3,54,54,7,456]
array2=[1,5,3,2,5,7,8,9,0,5,2,4,6,78,3,54,6,3,54,54,7,456]
print(len(array))

n=0
for x   in  range(len(array)-1,-1,-1):   
    b=True
    if  b==True:
        b=False
        for y   in  range(0,x,1):
            if  array[y]>array[y+1]:
                temp=array[y]
                array[y]=array[y+1]
                array[y+1]=temp
                b=True
                n=n+1
 
print("n:"+str(n))

m=0
for x   in  range(len(array2)-1,-1,-1):    
    for y   in  range(0,x,1):
        if  array2[y]>array2[y+1]:
            temp=array2[y]
            array2[y]=array2[y+1]
            array2[y+1]=temp
            m=m+1
print("m:"+str(m))

for x   in  range(0,len(array),1):
    print(x,array[x])

