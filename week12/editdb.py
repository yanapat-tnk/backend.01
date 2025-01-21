import database
mycursor = database.mydb.cursor()

def editdb(table):
    if table == "student":
        id = int(input('ใส่เลขไอดีที่ต้องการเปลี่ยน :'))
        call = input('ใส่คอลัมที่ต้องการจะเปลี่ยน :')
        val1 = input('ใส่ค่าที่ต้องการเปลี่ยน')
        sql = f"UPDATE student SET {call} = %s WHERE id = %s"
        val = (val1,id)
        mycursor.execute(sql,val)
        database.mydb.commit()
        if mycursor.rowcount <= 0 :
            print('ผิดพลาด')
        else:
            print('สำเร็จ')

editdb("student")