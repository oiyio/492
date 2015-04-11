# first MariaDB connection with python in ubuntu

#!/usr/bin/python
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='1', database='db1')
cursor = mariadb_connection.cursor()

#retrieving information
some_name = 'Georgi'
cursor.execute("SELECT * FROM Employees")


data = cursor.fetchone()

print (data)

mariadb_connection.close()
