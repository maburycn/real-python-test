#!/usr/bin/python3

import sqlite3

#create a connection
conn = sqlite3.connect("new.db")

#get a cursor
cursor = conn.cursor()

#incert a data
cursor.execute("INSERT INTO population VALUES('New York City',\
                  'NY',8400000)")
cursor.execute("INSERT INTO population VALUES('San Francisco',\
                  'CA',8000000)")

#IMPORTANT, need to commit first
conn.commit()

#close
conn.close()
