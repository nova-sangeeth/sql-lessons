import pandas as pd
import os
import sqlite3



if os.path.exists('sqlite3.db'):
    os.remove('sqlite3.db')

connection = sqlite3.connect('sqlite3.db')

cur = connection.cursor()

def execute(queryString):
    connection.execute(queryString)
    connection.commit()
