#!/usr/bin/python3


import sqlite3

with sqlite3.connect("homework01.db") as conn:
    m = conn.cursor()

    #insert with values
    m.execute("INSERT INTO inventory VALUES('Fords','US',100)")
    m.execute("INSERT INTO inventory VALUES('Hondas','JP',200)")
    m.execute("INSERT INTO inventory VALUES('Hondas','JP',300)")

