import pymysql 

# Open database connection
db = pymysql.connect(user = "root", password = "root",
                     host = "127.0.0.1",
                     database = "quora" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS MOVIES")

# Create table as per requirement
sql = """CREATE TABLE MOVIES (
   Title  CHAR(20) NOT NULL,
   Text CHAR(20) )"""

cursor.execute(sql)

# disconnect from server
db.close()
