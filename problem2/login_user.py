import sqlite3
connection = sqlite3.connect('store_transaction.db')

cursor=connection.cursor()
#cursor.execute('''CREATE TABLE USERNAME
             #([generated_id] INTEGER PRIMARY KEY,username text,password text)''')
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
