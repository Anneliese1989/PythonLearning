import Pythonlearn
 

class FileIO(object):
    def FileIO(self,filenames,lines):
        try:
           file=open(filenames,"wb")
           #file=open(filenames,"ab")
           for x in range(10):
               file.writelines(lines)
               
           file=open(filenames,"rb") 
           print file.readlines()            
        except Error as e:
            print(e)
        
 
        finally:
            
            print "finally i did it"
        
    
    def FileIO2(cls,filenames,lines):
        try:
           file=open(filenames,"wb")
          
           for x in range(10):
               file.writelines(lines)
               
           file=open(filenames,"rb") 
           print file.readlines()            
        except Error as e:
            print(e)
        
 
        finally:
            
            print "finally i did it 2"

 
if __name__ == '__main__':
    fio=FileIO()
    #for x in range(10):
    fio.FileIO2("record.log","this is the second IO method")
  
