#!/usr/bin/python3


import sqlite3

#create a databse named cars
conn = sqlite3.connect("homework01.db")

#Get a cursor
cursor = conn.cursor()

#operation on cursor
cursor.execute("""CREATE TABLE inventory
                  (Make TEXT,Model TEXT, Quantity INT)
               """)

#close
conn.close()
