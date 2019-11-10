import os
import sqlite3

clear = lambda: os.system('cls')
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

# set up projects table
sql = """
  CREATE TABLE IF NOT EXISTS projects(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    priority TEXT
  )
"""

cur.execute(sql)
conn.commit()


# add dummy data for projects table
DEFAULT_NAME = "WORKON"
DEFAULT_PRIORITY = "complex"
sql_add = """
  INSERT INTO projects(name,priority)
  VALUES ("WORKON", "complex"),("REACT DASHBOARD", "medium"),("EMEASIAWM", "complex")
  """

cur.execute(sql_add)
conn.commit()