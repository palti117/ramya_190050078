import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

sql_create_table = '''CREATE TABLE users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);'''

def create_user(conn, user):
    sql = ''' INSERT INTO users(username,password,created_at)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid

conn = create_connection("user.db")
with conn:
    #create a user table
    cur = conn.cursor()
    cur.execute(sql_create_table)
    #inser user data
    user = ("ramya","welcome.1",None)
    user_id = create_user(conn,user)
    print(user_id)
    user2 = ("suma","welcome.2",None)
    user_id_2 = create_user(conn,user2)
    print(user_id_2)
