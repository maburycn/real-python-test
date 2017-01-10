#!/usr/bin/python3

import sqlite3


#create a new database if the database doesn't already exist
conn = sqlite3.connect("new.db")

#get a cursor object used to execute SQL commands
cursor = conn.cursor()

cursor.execute("""CREATE TABLE population
                 (city TEXT,stat TEXT,population INT)
               """)

#close the database connection
conn.close()
