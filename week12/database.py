import mysql.connector as mysqlcon
mydb = mysqlcon.connect(
    host = "localhost",
    user = 'root',
    password = "3009",
    database = 'students')

print(mydb)
