import os
import sqlite3
import pandas as pd

connection = sqlite3.connect('Chinook_Sqlite.sqlite')
cur = connection.cursor()


def execute(queryString):
  connection.execute(queryString)
  connection.commit()
  
def executemany(queryString,data):
  cur.executemany(queryString,data)
  connection.commit()

def read_sql(sql_query):
  return pd.read_sql(sql_query,connection)
