#!/usr/bin/python3

import sqlite3

with sqlite3.connect("homework01.db") as conn:
    m = conn.cursor()
    m.execute("SELECT * from inventory WHERE Make = 'Audi'")
    res = m.fetchall()
    for item in res:
        print (item[0],item[1],item[2])
