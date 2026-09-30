class BankAccount:
    def __init__(self, owner: str, balance: float, account_type: str):
        self._owner = owner              # Захищений атрибут
        self.__balance = 0.0             # Приватний атрибут
        self.balance = balance           # Використання сеттера для валідації
        self.account_type = account_type

    # Getter для балансу
    @property
    def balance(self) -> float:
        return self.__balance

    # Setter для балансу з валідацією
    @balance.setter
    def balance(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("Баланс повинен бути числом!")
        if value < 0:
            raise ValueError("Баланс не може бути від'ємним!")
        self.__balance = float(value)

    # Обчислювана властивість (read-only)
    @property
    def status(self) -> str:
        return "VIP" if self.__balance >= 10000 else "Standard"


if __name__ == "__main__":
    print("=== 1. Створення об'єкта з валідними даними ===")
    acc = BankAccount("Глеб", 5000.0, "Debit")
    print(f"Власник: {acc._owner}, Баланс: {acc.balance}, Статус: {acc.status}")

    print("\n=== 2. Перевірка обчислюваної властивості (read-only) ===")
    acc.balance = 15000.0  
    print(f"Новий баланс: {acc.balance}, Оновлений статус: {acc.status}")

    print("\n=== 3. Перехоплення помилок валідації (setter) ===")
    try:
        acc.balance = "багато"
    except TypeError as e:
        print(f"Поймано TypeError: {e}")

    try:
        acc.balance = -100
    except ValueError as e:
        print(f"Поймано ValueError: {e}")

    print("\n=== 4. Демонстрація name mangling та AttributeError ===")
    try:
        print(acc.__balance)
    except AttributeError:
        print("Помилка: прямий доступ до __balance неможливий (AttributeError)")

    print(f"Доступ через name mangling (_BankAccount__balance): {acc._BankAccount__balance}")