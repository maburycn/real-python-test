#!/usr/bin/python3

import sqlite3


with sqlite3.connect("homework01.db") as conn:
    m = conn.cursor()
    m.execute("""CREATE TABLE orders (Make TEXT,Model INT,Order_date STRING)""")
