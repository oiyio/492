# -*- coding: utf-8 -*-
# TESTING
#  import create_tables100 as cr
#  cr.create()
#  cr.test("ahmet123","12345678")

import sqlite3

def create():
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""CREATE TABLE users3(
					username VARCHAR(20) NOT NULL, 
					password VARCHAR(20) NOT NULL,
					password2 VARCHAR(20) NOT NULL,
					password3 VARCHAR(20) NOT NULL)""")

	veriler = [
				("ahmet123", "12345678","12345678","12345678"),
				("mehmet321", "87654321","12345678","12345678"),
				("selin456", "123123123","12345678","12345678")
			  ]

	for i in veriler:
		im.execute("""INSERT INTO users3 VALUES (?, ?, ?, ?)""", i)

	db.commit()

def test(username,password):	
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""SELECT * FROM users3 WHERE
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