class Money:
    def __init__(self, amount: float, currency: str = "UAH"):
        self.amount = float(amount)
        self.currency = currency

    # 1. Представлення (__str__)
    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"

    # 2. Представлення (__repr__)
    def __repr__(self) -> str:
        return f"Money(amount={self.amount}, currency='{self.currency}')"

    # 3. Арифметика: додавання (__add__)
    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    # 4. Арифметика: віднімання (__sub__)
    def __sub__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount - other.amount, self.currency)

    # 5. Порівняння: рівність (__eq__)
    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return False
        return self.amount == other.amount and self.currency == other.currency

    # 6. Контейнер/інше: модуль числа (__abs__)
    def __abs__(self):
        return Money(abs(self.amount), self.currency)


if __name__ == "__main__":
    wallet1 = Money(1500.50, "UAH")
    wallet2 = Money(300.25, "UAH")
    debt = Money(-500.0, "UAH")

    print("=== 1. Магічні методи __str__ та __repr__ ===")
    print(f"Вивід через print (__str__): {wallet1}")
    print(f"Вивід через repr() (__repr__): {repr(wallet1)}")

    print("\n=== 2. Арифметичні оператори (+ та -) ===")
    print(f"Додавання: {wallet1} + {wallet2} = {wallet1 + wallet2}")
    print(f"Віднімання: {wallet1} - {wallet2} = {wallet1 - wallet2}")

    print("\n=== 3. Оператор порівняння (==) ===")
    wallet3 = Money(1500.50, "UAH")
    print(f"{wallet1} == {wallet3}: {wallet1 == wallet3}")
    print(f"{wallet1} == {wallet2}: {wallet1 == wallet2}")

    print("\n=== 4. Вбудована функція abs() (__abs__) ===")
    print(f"Початкове значення: {debt}")
    print(f"Після застосування abs(): {abs(debt)}")