import pymysql
 
def create_user_data(n):
    users = []
    for i in range(n):
        username = 'user'+ str(i+1)
        users.append((username , '000000'))
    return users
 
 
db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
cur = db.cursor()
 
insert_sql = 'insert into userinfo values(%s,%s)'
users = create_user_data(100)
cur.executemany(insert_sql,users)

db.commit()
cur.close()
db.close()
