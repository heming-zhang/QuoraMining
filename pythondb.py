import pymysql 
import time

class DataBase():

   def __init__(self, rank, questionlink, timestamp, answercount, question, answertext):
      self.rank = rank
      self.questionlink = questionlink
      self.timestamp = timestamp
      self.answercount = answercount
      self.question = question
      self.answertext = answertext

   # def insert_link(self):
   #    rank = self.rank
   #    questionlink = self.questionlink
   #    timestamp = self.timestamp
   #    questionlinks = []
   #    questionlinks.append((rank, questionlink, timestamp))
   #     # Open database connection
   #    db = pymysql.connect(user = "root", password = "root",
   #                         host = "127.0.0.1",
   #                         database = "quora" )
   #    # prepare a cursor object using cursor() method
   #    cursor = db.cursor()
   #    sql = """insert into questionlinks values(%s, %s, %s)"""
   #    cursor.executemany(sql, questionlinks)
   #    # disconnect from server
   #    db.close()
   

   def insert_link(self):
      # to place into single table without repetition
      rank = self.rank
      questionlink = self.questionlink
      timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + self.timestamp
      questionlinks = []
      questionlinks.append((rank, questionlink, timestamp))
       # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      # use loop to prevent repetition
      for questionlink0 in questionlinks:
         try:
            sql = """insert into questionlinks values(%s, %s, %s)"""
            cursor.execute(sql, questionlink0)
         except Exception:
            print("repetition", Exception)
            continue
      # disconnect from server
      db.close()
   

   def select_links(self):
      # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      sql = """select * from questionlinks order by rank"""
      cursor.execute(sql)
      questionlinks = cursor.fetchall()
      db.close()
      return questionlinks

   def insert_content(self):
      rank = self.rank
      answercount = self.answercount
      timestamp = self.timestamp
      questionlink = self.questionlink
      question = self.question
      answertext = self.answertext
      movies = []
      movies.append((rank, answercount, timestamp, questionlink, question, answertext))
       # Open database connection
      db = pymysql.connect(user = "root", password = "root",
                           host = "127.0.0.1",
                           database = "quora" )
      # prepare a cursor object using cursor() method
      cursor = db.cursor()
      sql = """insert into movies values(%s, %s, %s, %s, %s, %s)"""
      cursor.executemany(sql, movies)
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
      cursor.execute("drop table if exists questionlinks")
      # Create table as per requirement
      sql = """create table questionlinks (
         rank int,
         questionlink varchar(200) primary key, 
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
      cursor.execute("drop table if exists movies")
      # Create table as per requirement
      sql = """create table movies(
         rank int not null,
         answercount int,
         timestamp varchar(50),
         questionlink varchar(200),
         question  varchar(200),
         answertext varchar(65533))"""
      cursor.execute(sql)
      # disconnect from server
      db.close()

