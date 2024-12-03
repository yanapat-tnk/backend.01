import shopping
mycursor = shopping.mydb.cursor()
  
def show_table():
    mycursor.execute("SHOW TABLE")
    table = mycursor.fetchall()
    print('เนื้อหาทั้งหมด')
    for i in table:
        print(i)

def select_all():
    show_table()
    table = input('ใส่หัวข้อที่จะค้นหา :')
    mycursor.execute(f"SELECT * FROM {table}")
    myresulf = mycursor.fetchall()
    for i in myresulf:
        print(i)

def select_users():
   name = input('ต้องการไรจ๊ะ :')
   mycursor.execute(f"SELECT * FROM users where username like '%{name}%' ") 
   myresulf = mycursor.fetchall()
   for i in myresulf:
        print(i)

def select_products():
   name = input('ต้องการไรจ๊ะ :')
   mycursor.execute(f"SELECT * FROM products where product_name like '%{name}%' ") 
   myresulf = mycursor.fetchall()
   for i in myresulf:
        print(i)

def select_categories():
   name = input('ต้องการไรจ๊ะ :')
   mycursor.execute(f"SELECT * FROM categories where category_name like '%{name}%' ") 
   myresulf = mycursor.fetchall()
   for i in myresulf:
        print(i)

def select_orders():
   name = input('ต้องการไรจ๊ะ :')
   mycursor.execute(f"SELECT * FROM orders where order_id like '%{id}%' ") 
   myresulf = mycursor.fetchall()
   for i in myresulf:
        print(i)

select_categories()