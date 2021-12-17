import mysql.connector
import os
import xlrd
import pandas 
import sqlalchemy
import xlwt

#Database connections:
hostname = input("database_connection_string")
username = input("username")
password = input ("password")


connection = mysql.connector.connect(host = 'database-3.c0fffrbsh5q8.ap-south-1.rds.amazonaws.com', user = 'username', password = 'password', database = input("database"))


#Read Excel files
datas = xlrd.open_workbook('./venkat.xls')
print(datas)
sheet = datas.sheet_by_index(0)
print(sheet)



#check the information of database server
mysql = connection.get_server_info()

print(mysql)

#cursor object is used to execute the query in database
mycursor = connection.cursor()
mycursor.execute("USE venkat;")
query = """INSERT INTO venkats(Number, Parent, Task_type, Priority) VALUES (%s,%s,%s,%s)"""

for r in range (0, sheet.nrows):
    Number = sheet.cell(r,0).value
    Parent = sheet.cell(r,1).value
    Task_type = sheet.cell(r,2).value
    Priority = sheet.cell(r,3).value
    values = (Number, Parent, Task_type, Priority)
    mycursor.execute(query, values)


mycursor.close()
connection.commit()
print ("connection established")
connection.close()
print ("connection closed")
