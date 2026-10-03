class Circle:
    def __init__(self, radius):
        self.__radius = radius  # รัศมีของวงกลม (Private)

    # Getter สำหรับรัศมี
    @property
    def radius(self):
        return self.__radius

    # Setter สำหรับรัศมี (ต้องเป็นค่าบวก)
    @radius.setter
    def radius(self, value):
        if value > 0:
            self.__radius = value
        else:
            print("Radius must be a positive number!")

    # คำนวณพื้นที่ของวงกลม
    def area(self):
        return 3.1416 * self.__radius ** 2  # คำนวณพื้นที่วงกลม

    # คำนวณรอบวงกลม
    def circumference(self):
        return 2 * 3.1416 * self.__radius  # คำนวณรอบวงกลม

# สร้างออบเจกต์ Circle
circle1 = Circle(5)

# แสดงรัศมี
print(f"Radius: {circle1.radius}")

# คำนวณพื้นที่และรอบวงกลม
print(f"Area: {circle1.area()}")
print(f"Circumference: {circle1.circumference()}")

# เปลี่ยนรัศมีโดยใช้ setter
circle1.radius = 10

# แสดงรัศมีใหม่
print(f"New Radius: {circle1.radius}")

# คำนวณพื้นที่และรอบวงกลมอีกครั้ง
print(f"New Area: {circle1.area()}")
print(f"New Circumference: {circle1.circumference()}")

# ทดสอบการตั้งค่ารัศมีเป็นค่าติดลบ
circle1.radius = -5  # จะได้รับข้อความ "Radius must be a positive number!"
