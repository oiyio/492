# -*- coding: utf-8 -*-
# some modification only this row
# some modification2 only this row
import sqlite3

def create():
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""CREATE TABLE users(
					username VARCHAR(20) NOT NULL, 
					password VARCHAR(20) NOT NULL)""")

	veriler = [
				("ahmet123", "12345678"),
				("mehmet321", "87654321"),
				("selin456", "123123123")
			  ]

	for i in veriler:
		im.execute("""INSERT INTO users VALUES (?, ?)""", i)

	db.commit()

	
def test(username,password):	
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""SELECT * FROM users WHERE
	username = ? AND password = ?""", (username, password))

	data = im.fetchone()

	if data:
		print (u"Welcome %s!" % data[0])

	else:
		print (u"Wrong username or password!")
		
if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	create()
	test()