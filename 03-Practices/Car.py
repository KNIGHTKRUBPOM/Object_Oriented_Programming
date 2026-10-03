class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print (f"แบรนด์ {self.brand} โมเดล {self.model} ปี {self.year}")
    
    def start_engine(self):
        print("Engine started")

    def stop_engine(self):
        print("Engine stopped")

car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

car1.display_info()
car2.display_info()

car1.start_engine()
car1.stop_engine()

car2.start_engine()
car2.stop_engine()