#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches
the argument.
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
        cursor.execute("SELECT * FROM states WHERE name LIKE \
        BINARY '{}';".format(argv[4]))

        list = cursor.fetchall()

        for item in list:
            print(item)

        cursor.close()
        DB_Conect.close()

    DBConection()
