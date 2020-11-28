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
insert_query2 = "INSERT INTO regions VALUES(2, 'CANADA', '002')"
insert_query3 = "INSERT INTO regions VALUES(3, 'AFRICA', '003')"

execute(queryString=insert_query)


# SELECT  STATEMENTS IN SQL

select_query = "select * from regions"
# execute(queryString=select_query)
# read_sql(select_query)
select_query_specific = "select * from regions where region_id = 2"
read_sql(select_query_specific)

# UPDATE METHODS IN SQL

updateQuery1 = "update regions set region_code = '003' where region_id = 2 "
execute(updateQuery1)
# read_sql("select * from regions")
updateQuery2 = "update regions set region_code = 004, region_name = 'America' where region_id = 2"
execute(updateQuery2)
# read_sql("select * from regions")


# DELETE query

del_query = "delete from regions where region_id = 1"

execute(queryString=del_query)


#drop_table

query_drop_table = "DROP TABLE regions"


# JOINS WITH MULTIPLE TABLE

query_dept_create = '''
CREATE TABLE departments(
    department_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    department_name text NOT NULL 
)
'''

execute(queryString=query_dept_create)


query_employee_create = '''
CREATE TABLE  employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    first_name text, 
    last_name text, 
    email text NOT NULL,
    phone_number text, 
    hire_date NOT NULL,
    emp_enroll_id INTEGER NOT NULL,
    salary double NOT NULL,
    manager_id integer, 
    dep_id integer,
    FOREIGN KEY (dep_id) REFERNCES departments (department_id),
    FOREIGN KEY (manager_id) REFERENCES employees (employee_id)
)
'''


execute(queryString=query_employee_create)

# ALTERING TABLES

dept_alter_query = '''
ALTER TABLE departments ADD security text
'''

execute(
    queryString=dept_alter_query
)

#insert data into dept

insert_dept = '''
insert into department(department_name) values(?)
'''
insert_dept_data = [
    ('Admin'),
    ('Accoutns'),
    ('IT'),
    ('Production'),
    ('Purchasing'),
    ('Marketing')
]
executemany(insert_dept, insert_dept_data)

#inserting data into employees:

employee_insert = '''
INSERT INTO employees(
    employee_id,
    first_name,
    last_name,
    email,
    phone_number,
    hire_date,
    emp_enroll_id,
    salary,
    manager_id, 
    dep_id
)
VALUES (?,?,?,?,?,?,?,?,?,?)
'''
insert_emp_data=[(100,'Steven','King','steven.king@xyz.com','515.123.4567','1987-06-17',4,24000.00,0,1),
         (101,'Neena','Kochhar','neena.kochhar@xyz.com','515.123.4568','1989-09-21',5,17000.00,100,2),
         (102,'Lex','De Haan','lex.de haan@xyz.com','515.123.4569','1993-01-13',5,17000.00,100,3),
         (103,'Alexander','Hunold','alexander.hunold@xyz.com','590.423.4567','1990-01-03',9,9000.00,102,2),
         (104,'Bruce','Ernst','bruce.ernst@xyz.com','590.423.4568','1991-05-21',9,6000.00,103,1),
         (105,'David','Austin','david.austin@xyz.com','590.423.4569','1997-06-25',9,4800.00,103,None)]

executemany(employee_insert, insert_emp_data)


#desc order in sql

desc_query = "select * from employees order by salary DESC"
execute(desc_query)

#ascending order
asc_query = "select * from employees order by salary DESC, first_name ASC"
execute(asc_query)

#CROSS JOIN
cross_query = '''
SELECT COUNT(*)
FROM
employees Join departments
'''
execute(queryString=cross_query)
#CROSS JOIN TWO

cross_query2 = '''
SELECT employee_id, first_name, department_name FORM employees CROSS JOIN departments
'''
execute(queryString=cross_query2)

#INNER JOIN
inner_join_query = '''
SELECT employee_id, first_name, department_name from employees
INNER JOIN departments ON employee.dep_id = departments.department_id
'''
execute(queryString=inner_join_query)


#OUTER JOIN QUERY

outer_join_query = '''
SELECT employee_id, first_name, department_name from employees INNER JOIN departments 
on employees.dep_id = departments.department_id
'''

execute(queryString=outer_join_query)






