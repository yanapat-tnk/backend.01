import tkinter
import database
import apidb
mycursor = database.mydb.cursor()
def selectdb(): 
    table = table_input.get()
    mycursor.execute(f"SELECT * FROM {table} ")
    show = mycursor.fetchall()
    if len(show) <= 0 :
        return False,None
    else:
        return True,output_lable.configure(text=show)

def deletedb():
    table = table_input.get()
    id = del_input.get()
    sql = f"DELETE FROM {table} WHERE {id_name} = %s"
    val = (id,)
    mycursor.execute(sql,val)
    database.mydb.commit()
    if mycursor.rowcount <= 0 :
        return False,None
    else:
        return True,None
  
def opendel():
    de

#----------------------------------------------------------------------------------------#
program = tkinter.Tk()
program.title('โปรแกรมจัดการข้อมูล')
program.minsize(width=400,height=400)

program_lable = tkinter.Label(master=program ,text="พิมพ์ตารางที่ต้องการ")
program_lable.pack()

table_input = tkinter.Entry(master=program)
table_input.pack()

del_input = tkinter.Entry(master=program)#entry คือช่่องว่าง  
del_input.pack()

search_button = tkinter.Button(master=program ,text="ค้นหาตาราง",command=selectdb)
search_button.pack()

del_button = tkinter.Button(master=program ,text="ลบข้อมูล",command=selectdb)
del_button.pack()

output_lable = tkinter.Label(master=program,text="ผลการค้นหา")
output_lable.pack()

program.mainloop()