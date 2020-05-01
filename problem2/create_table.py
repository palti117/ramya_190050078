import sqlite3
connection = sqlite3.connect('store_transaction.db')

cursor=connection.cursor()
cursor.execute('''CREATE TABLE USERNAME
             ([generated_id] INTEGER PRIMARY KEY,username text,password text)''')
#insert values in table
cursor.execute("INSERT INTO USERNAME VALUES (1,'kutti','hihi')")
cursor.execute("INSERT INTO USERNAME VALUES (2,'suma','rami')")
cursor.execute("INSERT INTO USERNAME VALUES (3,'ramya','kutti')")
