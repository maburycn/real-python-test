#!/usr/bin/python3

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    #incert multiple records using a TUPLE
    cities = [
              ('Boston','MA',600000),
              ('Chicago','IL',2700000),
              ('Houston','TX',2100000),
              ('Phoenix','AX',1500000)
             ]

    #insert data into table
    c.executemany('INSERT INTO population VALUES(?,?,?)',cities)
