#!/usr/bin/python3

import sqlite3

with sqlite3.connect("homework01.db") as conn:
    m = conn.cursor()

    m.execute("DELETE FROM inventory WHERE Make = 'Fords'")
    m.execute("DELETE FROM inventory WHERE Make = 'MX5'")
