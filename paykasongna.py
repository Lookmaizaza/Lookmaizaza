print("สวัสดี ฉันคือโปรแกรมคำนวณค่าขนส่งสินค้า")
print("ฉันช่วยคุณคิดราคาได้เมื่อน้ำหนักสูงสุดคือ 6 กก. เท่านั้น")

kg = int(input("ป้อนน้ำหนักสินค้า(กก.) : "))
ct = int(input("ป้อนปริมาตรกล่อง(ตร.ซม.) : "))
price = 0

if kg == 1:
   price += 25
if ct > 40:
   price += 25

if kg > 2:
    a_kg = (kg - 2)
if ct > 50:
    b_ct = (ct - 50)
    price += a_kg+b_ct * 5
    kg -= a_kg
    ct -= b_ct

if kg > 3:
    a_kg = (kg - 3)
if ct > 60:
    b_ct = (ct - 60)
    price += a_kg+b_ct * 6
    kg -= a_kg
    ct -= b_ct
 
if kg > 4:
    a_kg = (kg - 4)
if ct > 70:
    b_ct = (ct - 70)
    price += a_kg+b_ct * 7
    kg -= a_kg
    ct -= b_ct
 
if kg > 5:
    a_kg = (kg - 5)
if ct > 80:
    b_ct = (ct - 80)
    price += a_kg+b_ct * 8
    kg -= a_kg
    ct -= b_ct
 
if kg > 6:
    a_kg = (kg - 6)
if ct > 80:
    b_ct = (ct - 80)
    price += a_kg+b_ct * 9
    kg -= a_kg
    ct -= b_ct
 
if round(price) % 2 == 0:
    price += 0.5
 
print("ค่าส่งสินค้าราคา %s บาท" %price)
