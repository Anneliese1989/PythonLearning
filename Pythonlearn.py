# created date 2016-8-30

import io

import mysql.connector
from mysql.connector import errorcode

def connect():
    #""" Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='testschema',
                                       user='root',
                                       password='115100jjc')
        if conn.is_connected():
            print('Connected to MySQL database')
            curosor=conn.cursor()
            query = ("select * from student")
            #hire_start = datetime.date(1999, 1, 1)
            #hire_end = datetime.date(1999, 12, 31)
            curosor.execute(query)
            list=[]
            for (stu_id,stu_name,stu_guid,stu_Address) in curosor:
                list.append([stu_id,stu_name,stu_guid,stu_Address])

            for (stu_id,stu_name,stu_guid,stu_Address) in list:
                print stu_id,stu_name,stu_guid,stu_Address
     
         
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()