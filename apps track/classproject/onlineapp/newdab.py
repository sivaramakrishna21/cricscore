import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="Root@123")

mycursor=db.cursor()

mycursor.execute("create database onlinedb")