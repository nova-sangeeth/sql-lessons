from sqlite3.dbapi2 import connect
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

def executemany(queryString, data):
    cur.executemany(queryString,data)
    connection.commit()

def read_sql(sql_query):
    return pd.read_sql(sql_query, connection)

def list_tables():
    return read_sql("SELECT * FROM sqlite_master WHERE type='table' and name not like 'sqlite_%' ORDER BY name;")


query1 = '''
CREATE TABLE countries (
    country_id INTEGER PRIMARY KEY NOT NULL, 
    region_id INTEGER NO NULL, 
    country_growthRate decimal(5,2) DEFAULT 0,
    FOREIGN KEY (region_id) REFERENCES
    regions (region_id) ON DELETE CASCADE ON UPDATE CASCADE
)
'''
execute(queryString=query1)

query2 = '''
CREATE TABLE regions (
    region_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, region_name varchar(20), region_code varchar(20)
)
'''
execute(queryString=query2)

# list_tables()

#  altering the table

query_alter = '''
ALTER TABLE countries ADD country_name text
'''

execute(queryString=query_alter)
insert_query = "insert into regions values(1,'test-regions', '001')"

execute(queryString=insert_query)