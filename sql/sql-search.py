#!/usr/bin/python3
#

import sqlite3

with sqlite3.connect("newnum.db") as conn:
    m = conn.cursor()
    prompt = """
             Select the operatoin that your want to perform[1-5]:
             1. Average
             2. Maximum
             3. Minimum
             4. Summary
             5. Exit
             """
    while True:
        ans = input(prompt)

        if ans in set(["1","2","3","4"]):
            operation = {1:"avg",2:"max",3:"min",4:"sum"}[int(ans)]
            
            #retrive data
            m.execute("SELECT {}(num) from numbers".format(operation))

            #get data by using fetchone()
            get = m.fetchone()

            print ('*' * 30)
            print (operation + ":   %f" % get[0])
            print ('*' * 30)

        elif ans == "5":
            print ("Exit")

            # quit the loop
            break
