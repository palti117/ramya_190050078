import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

conn = create_connection("user.db")
cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

username = input("enter the user name: ")
password = input("enter the password: ")

total = len(rows)
count =0
for row in rows:
    count += 1
    if row[1] == username:
        if row[2] == password:
            print(row[2])
            print("authentication successful for user {}".format(username))
        else:
            print("wrong password")
    elif count == total:
        print("username {} not found".format(username))