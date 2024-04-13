#!/usr/bin/env python3

"""" lists all the states in the db created """

import MySQLdb    # import the mysql module  
import sys      # import the sys module

if __name__ == "__main__":
    """ a script that lists all states from the database hbtn_0e_0_usa """
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])    # connect to the database
    cur = conn.cursor()   # instantiate a cursor obj
    cur.execute("SELECT * FROM states ORDER BY id ASC")    # execute the query
    rows = cur.fetchall()    # fetch all the rows
    for row in rows:    # loop through the rows
        print(row)    # print the row       
    cur.close()
    conn.close()    # close the connection


