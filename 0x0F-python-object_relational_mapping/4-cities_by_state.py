#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
        cursor.execute("SELECT cities.id, cities.name, \
        states.name FROM cities LEFT JOIN states ON \
        cities.state_id = states.id ORDER BY cities.id ASC;")

        list = cursor.fetchall()

        for item in list:
            print(item)

        cursor.close()
        DB_Conect.close()

    DBConection()
