#!/usr/bin/python3
"""
script that lists all states from database 'hbtn_0e_0_usa'
"""
import MySQLdb
import sys

if __name__ == '__main__':
        db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3])
            cur = db.cursor()
            cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id asc",
                        (sys.argv[4],))
            rows = cur.fetchall()
            for row in rows:
                if row[1] == sys.argv[4]:
                    print(row)
            cur.close()
            db.close()
