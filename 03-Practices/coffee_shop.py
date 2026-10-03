class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price} บาท"

class HotDrink(Drink):
    def __init__(self, name, price, temperature="ร้อน"):
        super().__init__(name, price)
        self.temperature = temperature
    
    def __str__(self):
        return f"{self.name} ({self.temperature}): {self.price} บาท"

class ColdDrink(Drink):
    def __init__(self, name, price, ice_level="ปกติ"):
        super().__init__(name, price)
        self.ice_level = ice_level
    
    def __str__(self):
        return f"{self.name} (เย็น, น้ำแข็ง {self.ice_level}): {self.price} บาท"

class Order:
    order_count = 0  # ตัวแปรคลาส ใช้นับจำนวนออเดอร์ทั้งหมด
    
    def __init__(self):
        Order.order_count += 1  # เพิ่มค่า order_count ทุกครั้งที่สร้างออเดอร์ใหม่
        self.order_id = Order.order_count  # กำหนด order_id ตามค่าปัจจุบันของ order_count
        self.drinks = []  # ลิสต์เก็บเครื่องดื่มในออเดอร์
    
    def add_drink(self, drink):
        self.drinks.append(drink)
    
    def get_total_price(self):
        return sum(drink.price for drink in self.drinks)
    
    def __str__(self):
        drinks_str = "\n".join(str(drink) for drink in self.drinks)
        return f"Order {self.order_id}:\n{drinks_str}\nTotal: {self.get_total_price()} บาท"

class CoffeeShop:
    def __init__(self):
        self.menu = []
        self.orders = []
    
    def add_drink_to_menu(self, drink):
        self.menu.append(drink)
    
    def create_order(self):
        order = Order()
        self.orders.append(order)
        return order
    
    def get_total_revenue(self):
        return sum(order.get_total_price() for order in self.orders)
    
    def __str__(self):
        menu_str = "\n".join(str(drink) for drink in self.menu)
        return f"--- เมนูร้าน ---\n{menu_str}\n--- รายรับรวม: {self.get_total_revenue()} บาท ---"

# สร้างเครื่องดื่ม
espresso = HotDrink("Espresso", 45)
cappuccino = HotDrink("Cappuccino", 55)
ice_latte = ColdDrink("Iced Latte", 60, "มาก")
ice_mocha = ColdDrink("Iced Mocha", 65, "น้อย")

# สร้างร้านกาแฟ
shop = CoffeeShop()

# เพิ่มเมนู
shop.add_drink_to_menu(espresso)
shop.add_drink_to_menu(cappuccino)
shop.add_drink_to_menu(ice_latte)
shop.add_drink_to_menu(ice_mocha)

# สร้างคำสั่งซื้อ
order1 = shop.create_order()
order1.add_drink(espresso)
order1.add_drink(ice_latte)

order2 = shop.create_order()
order2.add_drink(cappuccino)
order2.add_drink(ice_mocha)

# แสดงข้อมูลร้านและคำสั่งซื้อ
print(shop)
print(order1)
print(order2)