import database 
def select_all(table):
    mycursor = database.mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)
        
def select_nametable(table):
    mycursor = database.mydb.cursor()
    name = input('ป้อนชื่อที่ต้องการค้นหา')
    mycursor.execute(f"SELECT * FROM {table} where name like '%{name}'")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)


select_nametable("subject")