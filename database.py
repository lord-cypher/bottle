import sqlite3
# maybe call it database.db
con = sqlite3.connect('data.db') # Warning: This file is created in the current directory

# blog

con.execute("CREATE TABLE blog (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO blog (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
con.execute("INSERT INTO blog (task,status) VALUES ('Visit the Python website',1)")
con.execute("INSERT INTO blog (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
con.execute("INSERT INTO blog (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")


# login

con.execute("CREATE TABLE users (username char NOT NULL, password char NOT NULL)")
con.execute("INSERT INTO users (username, password) VALUES ('admin', 'password')")


# admin table?

con.execute("CREATE TABLE adminGuesses (text char NOT NULL)")

# how to make myself admin

con.commit()