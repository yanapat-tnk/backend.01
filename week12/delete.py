import database
import select
mycursor = database.mydb.cursor()
show = selectdb.select_all()
def delete():
    table = select.select_all
    sql = "DELETE FROM %s WHERE id = %s"
    id = int(input('.lj8jk :'))
    val = (id,)
    mycursor.execute(sql,val)
    database.mydb.commit()
    selectdb.select_table(table)

delete()