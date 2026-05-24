VALID_CATEGORIES = ["Drinks", "Fast Food", "Desserts"]


class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        if category not in VALID_CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(VALID_CATEGORIES)}")

        self.__name = name.strip()
        self.__price = price
        self.__category = category

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_category(self) -> str:
        return self.__category

    def set_price(self, price: float):
        if price <= 0:
            raise ValueError("Price must be greater than zero.")
        self.__price = price

    def set_category(self, category: str):
        if category not in VALID_CATEGORIES:
            raise ValueError(f"Category must be one of: {', '.join(VALID_CATEGORIES)}")
        self.__category = category

    def display(self):
        print(f"  {self.__name:<20} Rs.{self.__price:>7.2f}   [{self.__category}]")

    def to_file_string(self) -> str:
        return f"{self.__name},{self.__price},{self.__category}"

    @staticmethod
    def from_file_string(line: str) -> "MenuItem":
        parts = line.strip().split(",")
        if len(parts) != 3:
            raise ValueError(f"Invalid menu item format: {line}")
        return MenuItem(parts[0], float(parts[1]), parts[2])

    def __str__(self):
        return f"{self.__name} - Rs.{self.__price:.2f} ({self.__category})"
