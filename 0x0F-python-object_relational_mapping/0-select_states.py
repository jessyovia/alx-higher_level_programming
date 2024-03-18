#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
