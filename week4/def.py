def choice_area_Rock_Paper_Scissors():
    while True:
        a = int(input("เลือกว่าจะทำอะไร \n1 คือ เป่ายิงฉุบ \n2 หาพื้นที่ \n0 คือ หยุดการทำงาน \n :"))
        if a == 1 :
            print(choice_Rock_Paper_Scissors())
        elif a == 2:
            print(choice_area())
        else :
            break

def choice_Rock_Paper_Scissors():
    while True:
        a = int(input("เลือกว่าจะเล่นต่อหรือไม่ \n1 คือ เล่น \n0 ย้อนกลับ \n :"))
        if a == 1 :
            print(Rock_Paper_Scissors())
        else :
            return


def Rock_Paper_Scissors() :
    import random
    print ("โปรแกรมเป่ายิงฉุบ")
    while True:
        a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
        b = input("เลือก ค้อน กรรไกร กระดาษ:")
        if b == a :
           print ("always")
        elif (a == "กรรไกร" and  b == "ค้อน") or (a == "กระดาษ" and  b == "กรรไกร") or (a == "ค้อน" and  b == "กระดาษ") :
            print ("You win!")
            print (choice_Rock_Paper_Scissors())
        else :
            print ("You lose!")

def choice_area():
    while True:
        a = int(input("เลือกว่าทำอะไร \n1 คือ หาพื้นที่ 4 เหลี่ยมจัตุรัส \n2 คือ หาพื้นที่ 4 เหลี่ยมผืนผ้า \n3 คือ หาพื้นที่วงกลม \n0 คือ ย้อนกลับ \n :"))
        if a == 1 :
            print(area_square())
        elif a == 2:
            print(area_rectanglr())
        elif a == 3:
            print(area_circle())
        else:
            return

def area_rectanglr():
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมผืนผ้า")
    wide = int (input("ใส่ความกว้าง :"))
    long = int (input("ใส่ความยาว :"))
    wl = wide * long
    print(f'ผลลัพธ์ของพื้นที่สี่เหลี่ยมผืนผ้า = {wl} \n')

def area_square():
    print("โปรแกรมคำนวณหาพื้นที่ 4 เหลี่ยมจัดุรัส")
    side = int(input("ใส่ด้าน : "))
    s = side * side
    print(f'ผลลัพธ์ของพื้นที่สี่เหลี่ยมจัดุรัส = {s} \n')

def area_circle():
    print("โปรแกรมคำนวณหาพื้นที่วงกลม")
    r = float (input("ใส่รัศมี:"))
    p = 3.14 * (r**2)
    print(f'ผลลัพธ์ของพื้นที่วงกลม = {p} \n')

print(choice_area_Rock_Paper_Scissors())