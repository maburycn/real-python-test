#!/usr/bin/python3
#Using with method, it will automatically commit after insert, so this is 
#not necessary to using commit again
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO population VALUES('New York City',\
                  'NY',8400000)")
    cursor.execute("INSERT INTO population VALUES('San Francisco',\
                  'CA',8000000)")

