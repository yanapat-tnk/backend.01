print ('กรุณากรอกข้อมูลส่วนตัว')
name = input("กรุณากรอกชื่อ\n")
age = input("กรุณากรอกอายุ\n")
id = input("กรุณากรอกรหัสประจ่าตัวนักศึกษา\n")
classyear = input("กรุณากรอกชั้นปี\n")
nickname = input("กรุณากรอกชื่อเล่น\n")
height = float(input("กรุณากรอกส่วนสูง\n"))
weight = float(input("กรุณากรอกนํ้าหนัก\n"))
hw = height+weight
print("ประวัติโดยย่อ")
print(f"ชื่อ : {name} อายุ : {age} ปี" )
print(f"รหัสประจำตัวนักศึกษา :  {id}ชั้นปีที่ :   {classyear}")
print("ชื่อเล่น : " + nickname)
print(f"ส่วนสูง :  {str(height)} เซนติเมตร น้ำหนัก :  {str(weight)} กิโลกรัม")
print(f"ส่วนสูง+น้ำหนัก = {str(hw)}")