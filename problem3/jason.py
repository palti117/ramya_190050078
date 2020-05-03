import pymysql, os, json
file = os.path.abspath('../../..') + "/model.json"
json_data=open(file).read()
json_obj = json.loads(json_data)
def validate_string(val):
   if val != None:
        if type(val) is int:
            #for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val
con = pymysql.connect(host = 'localhost:3306',user = 'root',passwd = '',db = 'user-password')
cursor = con.cursor()
for i, item in enumerate(json_obj):
    username = validate_string(item.get("username", None))
    password = validate_string(item.get("password", None))
    name = validate_string(item.get("name", None))
    cursor.execute("INSERT INTO user-password (username,	password,	name) VALUES (%s,	%s,	%s)", (username,	password,	name))
con.commit()
con.close()
