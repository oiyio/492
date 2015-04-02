# -*- coding: utf-8 -*-
######   testing in shell ######
#####
# import create_tables101 as cr
# cr.create()
# cr.insert()
# cr.test("ali","123")
# cr.printAll()

import sqlite3

# show all tables inside a selected database.
def show(): 
	db = sqlite3.connect("mydb2.db")
	im = db.cursor()
	im.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
	veriler = im.fetchall()
	print (veriler)
	

def create():
	db = sqlite3.connect("mydb2.db")

	im = db.cursor()

	im.execute("""CREATE TABLE users8(
					user_id INTEGER PRIMARY KEY AUTOINCREMENT,
					username VARCHAR(20) NOT NULL,
					password VARCHAR(20) NOT NULL,
					fullname VARCHAR(30) NOT NULL,
					email VARCHAR(30) NOT NULL
					)""")
					
def insert():

	db = sqlite3.connect("mydb2.db")
	im = db.cursor()
	
	veriler = [
				("ali","123","sanane","some@some"),
				("omer","123","sanane","some@some"),
				("ahmet","123","sanane","some@some"),
				("huseyin","123","sanane","some@some"),
				("kemal","123","sanane","some@some"),
				("cagdas","123","sanane","some@some")
			  ]
	#skip user_id, bacause of autoincrement, thus NULL in mysql command.
	for i in veriler:
		im.execute("""INSERT INTO users8 
		VALUES (NULL, ?, ?, ?, ?)""", i)

	db.commit()

	
def test(username,password):	
	db = sqlite3.connect("mydb2.db")

	im = db.cursor()

	im.execute("""SELECT * FROM users8 WHERE
	username = ? AND password = ?""", (username, password))

	data = im.fetchone()

	if data:
		print (u"Welcome %s !" % data[1])

	else:
		print (u"Wrong username or password!")
	
# -*- coding: utf-8 -*-

def printAll():
	vt = sqlite3.connect("mydb2.db")

	im = vt.cursor()

	im.execute("""SELECT * FROM users8""")

	veriler = im.fetchall()

	print (veriler)

	
	
if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	create()
	test()
	insert()
	printAll()