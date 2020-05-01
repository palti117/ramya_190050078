import sqlite3
connection = sqlite3.connect('store_transaction.db')

cursor=connection.cursor()
cursor.execute('''CREATE TABLE USERNAME
             ([generated_id] INTEGER PRIMARY KEY,username text,password text)''')