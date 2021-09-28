# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:22:05 2021

@author: F ANAME
"""


import mysql.connector

f = open("root.csv", "r") ; data= f.read()[3:21] ; user , ppw = data[:4] , data[5:]

mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  password=ppw,
  database='mydatabase'
)

mycursor = mydb.cursor()


mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
  

help(sqlalchemy)