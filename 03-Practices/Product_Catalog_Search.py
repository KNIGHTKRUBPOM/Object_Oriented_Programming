class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        self.__is_available = True

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class System:
    def __init__(self):
        self.__lst_product = []
        
    def add_product(self, product):
        self.__lst_product.append(product)

    def search(self, name):
        for product in self.__lst_product:
            if product.get_name().lower() == name.lower():
                return f"มีสินค้า : {product.get_name()}"
        else:
            return f"ไม่มีสินค้า : {name}"

system = System()
phone1 = Product("ปากกาไอแพด Apple Pencil Pro", "฿3,900")
phone2 = Product("Apple iPhone 13 128GB Midnight", "฿17,200")
phone3 = Product("Apple iPhone 16e 128GB Black", "฿22,900")
phone4 = Product("Apple iPhone 16e 128GB White", "฿22,900")
phone5 = Product("ร่ม Jisulife FA52 Portal Umbrella Fan Pink", "฿1,190")
phone6 = Product("Apple iPhone 16 Pro Max 256GB Desert Titanium", "฿46,400")
phone7 = Product("Apple Watch Series 10 GPS 42mm Rose Gold Aluminium Case with Light Blush Sport Band - S/M", "฿13,300")
phone8 = Product("Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue", "฿21,900")
phone9 = Product("สมาร์ทโฟน Samsung Galaxy S25 (12+512) Silver Shadow (5G)", "฿34,900")

system.add_product(phone1)
system.add_product(phone2)
system.add_product(phone3)
system.add_product(phone4)
system.add_product(phone5)
system.add_product(phone6)
system.add_product(phone7)
system.add_product(phone8)
system.add_product(phone9)

print(system.search("ปากกาไอแพด Apple Pencil Pro"))
print(system.search("Apple iPad Mini 7 (2024) Wi-Fi 256GB 8.3 inch Blue"))
print(system.search("Apple"))
