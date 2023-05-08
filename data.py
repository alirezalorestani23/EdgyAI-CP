import sqlite3
# import psycopg2

from models import User, threadParam

CREATE_ANALYSIS_TABLE = """
CREATE TABLE IF NOT EXISTS analysis_output (
  id INTEGER PRIMARY KEY,
  thread TEXT, 
  thread_id INTEGER,
  user_id INTEGER, 
  thread_intent TEXT,
  politeness INTEGER,
  acceptance INTEGER,
  explicit_words INTEGER,
  highlight_words INTEGER,
  engagement INTEGER,
  emotion INTEGER,
  trust INTEGER
  )
"""
ADD_THREAD = """
INSERT INTO analysis_output 
(thread, thread_id, user_id, thread_intent, politeness, acceptance, explicit_words,highlight_words, engagement, emotion, trust) 
VALUES (?,?,?,?,?,?,?,?,?,?,?)
"""

GET_ALL_THREADS = """
SELECT * FROM  analysis_output
"""
CREATE_USER_TABLE = """
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
"""

ADD_USER = """
INSERT INTO users (name,age) VALUES (?,?,?)
"""

GET_ALL_USERS = """
SELECT * FROM users
"""


def connect():
  # return psycopg2.connect(database="testdb", user="postgres", password="cohondob", host="127.0.0.1", port="5432")
  return sqlite3.connect("data.db")


def create_tables(connection):
  with connection:
    connection.execute(CREATE_USER_TABLE)
    connection.execute(CREATE_ANALYSIS_TABLE)


def add_user(connection, user: User):
  with connection:
    connection.execute(ADD_USER, (user.name, user.age))


def get_all_users(connection):
  with connection:
    return connection.execute(GET_ALL_USERS).fetchall()


def add_thread(connection, thread_parameters: threadParam.ThreadParam):
    with connection:
        connection.execute(ADD_THREAD, (thread_parameters.thread, thread_parameters.thread_id, thread_parameters.user_id,
                                        thread_parameters.thread_intent, thread_parameters.politeness,
                                        thread_parameters.acceptance,
                                        thread_parameters.explicit_words, thread_parameters.highlight_words,
                                        thread_parameters.engagement,
                                        thread_parameters.emotion, thread_parameters.trust))


def get_all_threads(connection):
  with connection:
    return connection.execute(GET_ALL_THREADS).fetchall()
