import mysql.connector

database = mysql.connector.Connect(
    host='localhost',
    user='root',
    password='PR12**iti'
)

cursorObject = database.cursor()

cursorObject.execute("create database testdb")

print("All done")