import database
mycursor = database.mydb.cursor() 
mycursor.execute("INSERT INTO subject VALUES ('7', 'Test2')")
database.mydb.commit() 