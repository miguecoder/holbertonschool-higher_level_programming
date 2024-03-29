#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


import MySQLdb
from sys import argv

if __name__ == "__main__":

    def DBConection():
        """
        Function that connects a database and print the"states" info
        """
        try:
            DB_Conect = MySQLdb.connect(
                "localhost",
                argv[1],
                argv[2],
                argv[3]
            )
        except Exception:
            print("Couldn't connect to database")
            return (0)

        cursor = DB_Conect.cursor()
        cursor.execute("SELECT * FROM states")

        list = cursor.fetchall()

        for item in list:
            print(item)

        cursor.close()
        DB_Conect.close()

    DBConection()
