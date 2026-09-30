from abc import ABC, abstractmethod

# 1. Абстрактний клас стратегії
class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, price: float) -> float:
        pass

# 2. Конкретні стратегії
class NoDiscount(DiscountStrategy):
    def calculate(self, price: float) -> float:
        return price

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def calculate(self, price: float) -> float:
        return price * (1 - self.percent / 100)

# Нова стратегія (демонстрація розширюваності без зміни іншого коду)
class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def calculate(self, price: float) -> float:
        return max(0.0, price - self.amount)

# 3. Контекстний клас, що використовує стратегію
class ShoppingCart:
    def __init__(self, price: float, strategy: DiscountStrategy):
        self.price = price
        self.strategy = strategy

    def set_strategy(self, strategy: DiscountStrategy):
        self.strategy = strategy

    def checkout(self) -> float:
        return self.strategy.calculate(self.price)

if __name__ == "__main__":
    original_price = 1000.0
    print(f"Початкова ціна товару: {original_price} грн\n")

    # Без знижки
    cart = ShoppingCart(original_price, NoDiscount())
    print(f"Звичайна ціна: {cart.checkout()} грн")

    # Зміна стратегії на відсоткову знижку (15%)
    cart.set_strategy(PercentageDiscount(15))
    print(f"Ціна зі знижкою 15%: {cart.checkout()} грн")

    # Додавання та використання нової стратегії (фіксована знижка 250 грн)
    cart.set_strategy(FixedDiscount(250))
    print(f"Ціна з фіксованою знижкою 250 грн: {cart.checkout()} грн")