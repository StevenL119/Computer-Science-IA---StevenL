import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="111"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Cycling")

