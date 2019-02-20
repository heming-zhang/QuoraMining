import pymysql 

class DataBase():

   def __init__(self, rank, questionlink, timestamp):
      self.rank = rank
      self.questionlink = questionlink
      self.timestamp = timestamp

   def insert_record(self):
      rank = self.rank
      questionlink = self.questionlink
      timestamp = self.timestamp
      movielinks = []
      movielinks.append((rank, questionlink, timestamp))
       # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      sql = """insert into movielinks values(%s, %s, %s)"""
      cursor.executemany(sql, movielinks)
      # disconnect from server
      db.close()
   
   def create_link_database(self):
      # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      # Drop table if it already exist using execute() method.
      cursor.execute("drop table if exists movielinks")
      # Create table as per requirement
      sql = """create table movielinks (
         rank int,
         questionlink varchar(200), 
         timestamp varchar(50))"""
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
      cursor.execute("drop table if exists movie")
      # Create table as per requirement
      sql = """create table movies(
         rank int not null,
         questionlink varchar(200),
         question  varchar(200),
         answer varchar(5000), 
         timestamp varchar(50))"""
      cursor.execute(sql)
      # disconnect from server
      db.close()




