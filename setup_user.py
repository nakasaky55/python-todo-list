import os
import sqlite3

clear = lambda: os.system('cls')
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

# set up projects table
sql  = """
  CREATE TABLE IF NOT EXISTS users(
    username TEXT NOT NULL,
    type INTEGER
  )
"""

cur.execute(sql)
conn.commit()


# add dummy data for projects table
sql_user = """
  INSERT INTO users(username, type)
  VALUES ("admin", 0)
  """

cur.execute(sql_user)
conn.commit()