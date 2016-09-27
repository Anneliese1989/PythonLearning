# created date 2016-8-30
# set the Sample Database to Utf-8 unicode collation  and update world.country set name='Réunion' where world.country.Code='REU'
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
            print('Connected to MySQL database\n')
            curosor=conn.cursor()
            query = ("SELECT Code,Name,Continent,Region FROM world.country where LifeExpectancy>70")
            #hire_start = datetime.date(1999, 1, 1)
            #hire_end = datetime.date(1999, 12, 31)
            curosor.execute(query)
            
            for  Code,Name,Continent,Region in curosor:
                #print  Code,Name,Continent,Region
                if "REU" in  repr(Code):
                     print  Code,Name,Continent,Region
                    #print repr(Code),repr(Name),repr(Continent),repr(Region)
                    #print repr(Code).decode("utf-8"),repr(Name).decode("utf-8"),repr(Continent).decode("utf-8"),repr(Region).decode("utf-8")
                    #print repr(Code).encode("utf-8"),repr(Name).encode("utf-8"),repr(Continent).encode("utf-8"),repr(Region).encode("utf-8")
                    
    except Error as e:
        print(e)
 
    finally:
        conn.close()
 
 
if __name__ == '__main__':
    connect()
