#!/usr/bin/env python3  

""""  list of states in the database hbtn_0e_0_usa where name matches the argument """
 
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], host="localhost", port=3306)
    match = sys.argv[4]
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id", (match,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
