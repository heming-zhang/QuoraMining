import pymysql 

class DataBase():

   def __init__(self, time):
      self.time = time

   def create_link_database(self):
       # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      # Drop table if it already exist using execute() method.
      cursor.execute("DROP TABLE IF EXISTS MOVIELINKS")
      # Create table as per requirement
      sql = """CREATE TABLE MOVIELINKS (
         NUMBER INT,
         Text VARCHAR, 
         Datetime DATE)"""
      cursor.execute(sql)
      # disconnect from server
      db.close()
   
   def create_final_database(self):
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
         Text CHAR(20), 
         Datetime DATE)"""
      cursor.execute(sql)
      # disconnect from server
      db.close()




