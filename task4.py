from abc import ABC, abstractmethod

class Logger:
    def log(self, msg): print(f"[LOG]: {msg}")

class Delivery(ABC):
    def __init__(self, address, weight):
        self.address, self.weight = address, weight
        self.logger = Logger()  # Композиція (has-a)

    @abstractmethod
    def calculate_cost(self): pass

    @property
    @abstractmethod
    def delivery_type(self): pass

    def common_info(self):
        self.logger.log(f"Доставка на {self.address}")
        return f"Адреса: {self.address}, Вага: {self.weight} кг"

class CourierDelivery(Delivery):
    @property
    def delivery_type(self): return "Кур'єр"
    def calculate_cost(self): return 100 + self.weight * 25

class PostDelivery(Delivery):
    @property
    def delivery_type(self): return "Пошта"
    def calculate_cost(self): return 50 + self.weight * 10

if __name__ == "__main__":
    try: Delivery("Тест", 1)
    except TypeError as e: print(f"Помилка створення абстрактного класу: {e}\n")

    for d in [CourierDelivery("Шевченка 10", 2), PostDelivery("Перемоги 50", 10)]:
        print(f"Тип: {d.delivery_type} | {d.common_info()} | Вартість: {d.calculate_cost()} грн")