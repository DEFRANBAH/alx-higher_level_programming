#!/usr/bin/env python3

"""Filter states by user input-prefference from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve the states
    cursor.execute("SELECT * FROM states WHERE name LIKE Binary 'N%' ORDER BY states.id ASC")

    # Fetch all the rows returned by the querytes
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
