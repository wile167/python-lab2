class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_info(self):
        return f"{self.brand}: до {self.speed} км/год"

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

    def get_info(self):
        return f"Авто {self.brand}, дверей: {self.doors}, швидкість: {self.speed} км/год"

class Bicycle(Vehicle):
    def __init__(self, brand, speed, gears):
        super().__init__(brand, speed)
        self.gears = gears

    def get_info(self):
        return f"Велосипед {self.brand}, швидкостей: {self.gears}, швидкість: {self.speed} км/год"

class Scooter(Vehicle):
    def __init__(self, brand, speed, battery):
        super().__init__(brand, speed)
        self.battery = battery

    def get_info(self):
        return f"Самокат {self.brand}, батарея: {self.battery}Вт·год, швидкість: {self.speed} км/год"

# Обов'язково мають бути ці рядки, щоб у терміналі щось з'явилося:
vehicles = [Car("Toyota", 180, 4), Bicycle("Giant", 30, 21), Scooter("Xiaomi", 25, 300)]

print("--- Поліморфний обхід ---")
for v in vehicles:
    print(v.get_info())

print("\n--- Перевірка типів ---")
print(isinstance(vehicles[0], Car))       # True
print(issubclass(Bicycle, Vehicle))     # True