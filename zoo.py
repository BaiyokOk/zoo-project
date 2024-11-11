class Zoo:
    def get_ticket_price(self, age):
        if age < 0:
            return "Invalid age" #เพิ่มเงื่อนไขเมื่อ age มีค่าน้อยกว่า 0
        elif 0 < age <= 12:
            return 50
        elif 13 <= age < 20: # แก้จาก < 20 เป็น <= 20
            return 100
        elif 21 <= age <= 60: # แก้จาก 21 < เป็น 21 <=
            return 150
        elif age > 60: # แก้จาก >= เป็น >
            return 100