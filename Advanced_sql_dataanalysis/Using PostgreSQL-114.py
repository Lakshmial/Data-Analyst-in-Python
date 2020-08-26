## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cursor = conn.cursor()
print(cursor)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cursor = conn.cursor()
cursor.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY, body TEXT,title TEXT)")
conn.close()                              


## 5. SQL Transactions ##

conn = psycopg2.connect("dbname=dq user=dq")
cursor = conn.cursor()
#cursor.execute ("CREATE TABLE notes(id integer PRIMARY KEY, body text, title text)")
cursor.execute("drop TABLE notes")
cursor.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY ,body TEXT,title TEXT)")
conn.commit()
conn.close()

## 6. Autocommitting ##

conn = psycopg2.connect("dbname=dq user=dq")
conn.autocommit =True
cursor = conn.cursor()
cursor.execute("drop TABLE facts")
cursor.execute("CREATE TABLE facts (id INTEGER PRIMARY KEY ,country TEXT,value TEXT)")
conn.close()

## 7. Executing queries ##

conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cursor=conn.cursor()
cursor.execute("DROP TABLE notes")
cursor.execute("CREATE TABLE notes(id INTEGER PRIMARY KEY ,body TEXT,title TEXT)")
cursor.execute("INSERT INTO notes VALUES(1,'Do more missions on Dataquest.','Dataquest reminder')")
cursor.execute("SELECT *FROM notes")
rows=cursor.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

conn =psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cursor=conn.cursor()
cursor.execute("DROP DATABASE income")
cursor.execute("CREATE DATABASE income OWNER dq")
conn.close()

## 9. Deleting a database ##

conn=psycopg2.connect("dbname=dq user=dq")
conn.autocommit=True
cursor=conn.cursor()
cursor.execute("DROP DATABASE income")
conn.close()