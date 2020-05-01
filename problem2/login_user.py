import sqlite3
connection = sqlite3.connect('store_transaction.db')

cursor=connection.cursor()
#cursor.execute('''CREATE TABLE USERNAME
             #([generated_id] INTEGER PRIMARY KEY,username text,password text)''')
#insert values in table
cursor.execute("INSERT INTO USERNAME VALUES (1,'kutti','hihi')")
cursor.execute("INSERT INTO USERNAME VALUES (2,'suma','rami')")
cursor.execute("INSERT INTO USERNAME VALUES (3,'ramya','kutti')")

cursor.execute("SELECT * FROM USERNAME")
results=cursor.fetchall()
user=input("Enter Username: ")
password=input("Enter password: ")
user2=list(filter(lambda x:user in x,results))
if(len(user2)==0):
	print("Login failed")
else:
	for x in user2:
		if(x[2]==password and x[1]==user):
			print("Login Successful")
			break
		elif(x==user2[len(user2)-1]):
			print("Password incorrect")
