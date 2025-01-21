import database
mycursor = database.mydb.cursor()

def selectdb(table):
    mycursor.execute(f"SELECT * FROM {table} ")
    show = mycursor.fetchall()
    if len(show) <= 0 :
        return False,None
    else:
        return True,show

#----------------------------------------------------------------------------------------#

#def deletedb(table,id,id_name):
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val = (id,)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
 
#----------------------------------------------------------------------------------------#

def insertdb(table):
    sql = "INSERT INTO users VALUES (%s, %s,%s, %s   v)"
    val = (id,)
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    if mycursor.rowcount <= 0 : 
        return False,None
    else:
        return True,None

#----------------------------------------------------------------------------------------#

def insertdb(table):
    sql = "INSERT INTO orders VALUES (%s, %s,%s, %s)"
    val = (id,)
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    if mycursor.rowcount <= 0 : 
        return False,None
    else:
        return True,None

#----------------------------------------------------------------------------------------#

def insertdb(table):
    sql = "INSERT INTO products VALUES (%s, %s,%s, %s)"
    val = (id,)
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    if mycursor.rowcount <= 0 : 
        return False,None
    else:
        return True,None

#----------------------------------------------------------------------------------------#

def insertdb(table):
    sql = "INSERT INTO categories VALUES (%s, %s,%s, %s)"
    val = (id,)
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    if mycursor.rowcount <= 0 : 
        return False,None
    else:
        return True,None

#----------------------------------------------------------------------------------------#
