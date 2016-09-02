# created date 2016-8-30
import io

import mysql.connector
from mysql.connector import errorcode

def connect():
    #""" Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='world',
                                       user='root',
                                       password='********')
        if conn.is_connected():
            print('Connected to MySQL database\n')
            curosor=conn.cursor()
            query = ("SELECT Code,Name,Continent,Region FROM world.country where LifeExpectancy>70")
            #hire_start = datetime.date(1999, 1, 1)
            #hire_end = datetime.date(1999, 12, 31)
            curosor.execute(query)
            
            for Code,Name,Continent,Region in curosor:
                print Code,Name,Continent,Region
    
    except errorcode as e:
        print(e)
 
    finally:
        conn.close()
 
if __name__ == '__main__':
    connect()
 
  
