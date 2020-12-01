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


#select statements

read_sql(
  "select * from Track limit 20"
)

#select Items from albums

select_query = 'select * from Album limit 10'


# SELECT RECORDS ACCORDING TO THE TIME OF EACH TRACK

query_select1 = '''
select
a.Title as AlbumTitle, t.Name as TrackName, (MilliSeconds/1000.60.0) as Minutes
from
Track t join Album a on (a.AlbumId = t.AlbumId)
LIMIT 10
'''

# ALBUM THAT HAS THE MAXIMUM NUMBER OF TRACKS
query_max_num = '''
select AlbumId, count(*) as albumcount
from Track
Group by AlbumId
'''

