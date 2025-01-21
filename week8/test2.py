import database

mycursor = database.mydb.cursor() 

def show_table():
    mycursor.execute("SHOW TABLE")
    table = mycursor.fetchall()
    print('เนื้อหาทั้งหมด')
    for i in table:
        print(i)

def select_all(table):
    mycursor = database.mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def subject():
    sql = "INSERT INTO subject VALUES (%s, %s)"
    a = int(input ("id_subject : "))
    b = str(input ("name_subject : "))
    val = (a, b)
    mycursor.execute(sql,val)

    database.mydb.commit() 

subject()