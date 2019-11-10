import os
import sqlite3
from colorama import init
from termcolor import colored
from tabulate import tabulate
import datetime

clear = lambda: os.system('cls')
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
DEFAULT_ID = ""
DEFAULT_STATUS = "uncomplete"
LOGGED_IN = False
init()
conn = sqlite3.connect(DEFAULT_PATH)
cur = conn.cursor()

sql = """
  CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY,
    body TEXT NOT NULL,
    difficulty INTEGER CHECK (difficulty <= 10),
    status TEXT NOT NULL,
    user_id INTEGER,
    created_at DATE
  )
"""

cur.execute(sql)
conn.commit()

# login menu
def print_login():
  print(colored('Enter your user name', 'green'))
  input_username = input()

  sql = """
  SELECT * FROM users
  WHERE username = ?
  """
  cur.execute(sql, (input_username,))
  result = cur.fetchone()
  if result == None:
    return False
  else:
    return input_username



# print menu
def print_menu():
  # os.system('cls' if os.name == 'nt' else 'clear')
  print(colored('Todo List Options:', 'green'))
  print(colored('*' * 50, 'green'))
  print(colored('1. List all todos:', 'green'))
  print(colored('2. Add a new todo:', 'green'))
  print(colored('3. Delete a todo:', 'green'))
  print(colored('4. Mark a todo complete:', 'green'))
  print(colored('5. Mark a todo uncomplete:', 'green'))
  print(colored('6. SIGN OUT', 'red'))
  print(colored('-' * 100, 'green'))

# add a record
def add():
  print("Enter your todo:")
  body = input()
  print("Estimate difficult: ")
  difficult = int(input())

  now = datetime.datetime.today().strftime('%d, %b %Y')

  sql = """
  INSERT INTO todos(body, user_id, difficulty, status, created_at)
  VALUES (?,?,?,?,?)
  """
  cur.execute(sql, (body, DEFAULT_ID, difficult, DEFAULT_STATUS, now,))
  conn.commit()

# list all mission
def list():
  sql = """
  SELECT * FROM todos
  WHERE user_id = ?
  """
  cur.execute(sql, (DEFAULT_ID,))
  result = cur.fetchall()
  print(tabulate(result, headers=[colored("id","green"),colored("mission","red"), colored("difficulty","yellow"),colored("status", "cyan"),  colored("user id", "magenta"),  colored("created_at", "red")], tablefmt="fancy_grid"))


# delete a record
def delete():
  print("Which todo you want to delete ? \t it must be an integer")
  id_to_del = int(input())

  sql_del = """
  DELETE FROM todos WHERE id = ?
  """

  cur.execute(sql_del, (id_to_del,))
  conn.commit()

#mark a todo as completed
def mark_complete():
  print("Which todo you want to mark as completed ? \n\t it must be an integer")
  id_to_complete = int(input())

  sql_complete = """
  UPDATE todos
  SET status = "completed"
  WHERE id = ?
  """

  cur.execute(sql_complete, (id_to_complete,))
  print(conn.commit, " commit complete")

#mark a todo as uncomplete
def mark_un_complete():
  print("Which todo you want to tell me that it's not done yet ? \n\t it must be an integer")
  id_to_complete = int(input())

  sql_complete = """
  UPDATE todos
  SET status = "uncomplete"
  WHERE id = ?
  """

  cur.execute(sql_complete, (id_to_complete,))
  conn.commit()

# main execute
if __name__ == '__main__':
  i = 0
  text = colored('Enter your id', 'red', attrs=['reverse', 'blink'])
  print(text)
  DEFAULT_ID = input()
  # try:
  while i == 0 and DEFAULT_ID != "":
    welcome = "Hello,"+DEFAULT_ID
    print(colored(welcome, 'red', attrs=['reverse', 'blink']))
    print_menu()

    choice = int(input())
    if choice == 1:
      list()
    elif choice == 2:
      add()
    elif choice == 3:
      delete()
    elif choice == 4:
      mark_complete()
    elif choice == 5:
      mark_un_complete()
    elif choice == 6:
      i -= -1
  # except:
  #   print("error")
