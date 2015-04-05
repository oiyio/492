# -*- coding: utf-8 -*-
######   testing in shell ######
#####
# import create_tables101 as cr
# cr.createAll()
# cr.insertToUser()
# cr.test("ali","123")
# cr.printAll()
# cr.showAllTables();
# cr.showAllRows();
# cr.deleteRowFromUsers("ali")
# deletion of tables are done via shell commands.
# deletion of database are done via manually deleting .db file.
import sqlite3

def createAll():
	createUsersTable()
	createPackagesTable()
	createCommentsTable()


def createUsersTable():
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""CREATE TABLE users(
					uid INTEGER PRIMARY KEY AUTOINCREMENT,
					username VARCHAR(20) NOT NULL,
					password VARCHAR(20) NOT NULL,
					fullname VARCHAR(30) NOT NULL,
					email VARCHAR(30) NOT NULL
					)""")
	im.execute("""CREATE INDEX uindex ON users (username)""")
	db.commit() # is it really necessary? 
	db.close()


# pid | package_name | category | total_rate | total_download	
def createPackagesTable():
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""CREATE TABLE packages(
					pid INTEGER PRIMARY KEY AUTOINCREMENT,
					pname VARCHAR(50) NOT NULL,
					version VARCHAR(50) NOT NULL,
					category VARCHAR(20) NOT NULL,
					total_rate INT NOT NULL,
					total_download INT NOT NULL
					)""")
					
	im.execute("""CREATE INDEX pindex ON packages (pname)""")
	
	db.commit()
	db.close()

def insertToPackages():

	db = sqlite3.connect("mydb.db")
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
		im.execute("""INSERT INTO packages 
		VALUES (NULL, ?, ?, ?, ?)""", i)

	db.commit()
	db.close()
		

def createCommentsTable():
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""CREATE TABLE comments(
					cid INTEGER PRIMARY KEY AUTOINCREMENT,
					username VARCHAR(50) NOT NULL,
					pname VARCHAR(50) NOT NULL,
					rate VARCHAR(20) NOT NULL,
					comment INT NOT NULL,
					date INT NOT NULL
					)""")
					
	im.execute("""CREATE INDEX cpindex ON comments (pname)""")
	
	db.commit()
	db.close()

def deleteRow(username):
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("DELETE FROM users WHERE username='" + username + "';" )
	print ("something")
	db.commit()
	db.close()
	
def insertToUser():

	db = sqlite3.connect("mydb.db")
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
		im.execute("""INSERT INTO users 
		VALUES (NULL, ?, ?, ?, ?)""", i)

	db.commit()
	db.close()
	
def test(username,password):	
	db = sqlite3.connect("mydb.db")

	im = db.cursor()

	im.execute("""SELECT * FROM users WHERE
	username = ? AND password = ?""", (username, password))

	data = im.fetchone()

	if data:
		print (u"Welcome %s !" % data[1])

	else:
		print (u"Wrong username or password!")
	db.close()
# -*- coding: utf-8 -*-

# show all rows inside a table.
def showAllRows():
	vt = sqlite3.connect("mydb.db")

	im = vt.cursor()

	im.execute("""SELECT * FROM users""")

	veriler = im.fetchall()

	print (veriler)
	vt.close()
	
# show all tables inside a selected database.
def showAllTables(): 
	db = sqlite3.connect("mydb.db")
	im = db.cursor()
	im.execute("""SELECT name FROM sqlite_master WHERE type='table'""")
	veriler = im.fetchall()
	print (veriler)
	db.close()


if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
	create()
	test()
	insert()
	printAll()