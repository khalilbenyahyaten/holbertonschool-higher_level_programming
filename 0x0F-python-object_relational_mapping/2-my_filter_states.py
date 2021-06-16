#!/usr/bin/python3
"""
display all values state table
"""
import MySQLdb
import sys


def print_all_names():
    database = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=sys.argv[1],
                               passwd=sys.argv[2],
                               db=sys.argv[3],
                               charset="utf8"
                               )
    cur = database.cursor()
    search = sys.argv[4]
    query = """SELECT * FROM states WHERE name = '{:s}'
        ORDER BY id ASC""".format(search)
    cur.execute(query)
    row = cur.fetchall()
    for i in row:
        if i[1] == search:
            print(i)
    cur.close()
    database.close()


if __name__ == "__main__":
    print_all_names()
