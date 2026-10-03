class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class ShoppingCart:
    def __init__(self):
        self.item = []
    
    def add_product(self, product):
        self.item.append(product)
        print(f"{product.name} ลงตระกร้า")

    def get_total_price(self):
        return sum(item.price for item in self.item)
    
product1 = Product("Laptop", 25000)
product2 = Product("Mouse", 500)

cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)

print(f"ราคารวมทั้งหมด: {cart.get_total_price()} บาท")