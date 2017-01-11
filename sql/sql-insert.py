#!/usr/bin/python3


import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    oper = connection.cursor()
    #del database table if exist
    oper.execute("DROP TABLE if exists numbers")
    #create database table
    oper.execute("""CREATE TABLE numbers(num INT)""")
    #loop for 100 times
    for item in range(100):
        oper.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
