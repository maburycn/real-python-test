#!/usr/bin/python3
#


import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    #open the csv file and assigne it to a variable 
    employees = csv.reader(open("/tmp/employees.csv","rU"))
    
    c.execute("CREATE TABLE  employees(firstname TEXT,lastname TEXT)")

    c.executemany("INSERT INTO  employees(firstname,lastname)values(?,?)",employees)



