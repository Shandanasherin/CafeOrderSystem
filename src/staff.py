from person import Person
from menu_item import MenuItem, VALID_CATEGORIES
import os

MENU_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "menu.txt")


class Staff(Person):
    def __init__(self, name: str, username: str, password: str):
        super().__init__(name)
        self.__username = username
        self.__password = password

    def get_username(self) -> str:
        return self.__username

    def authenticate(self, password: str) -> bool:
        return self.__password == password

    def manage_menu(self, menu: list[MenuItem]):
        while True:
            print("\n  +---- Staff Menu Management ----+")
            print("  | 1. Add new item               |")
            print("  | 2. Remove item                |")
            print("  | 3. Update item price          |")
            print("  | 4. Display full menu          |")
            print("  | 5. Save menu to file          |")
            print("  | 6. Back to main menu          |")
            print("  +-------------------------------+")
            choice = input("  Select option: ").strip()

            if choice == "1":
                self._add_item(menu)
            elif choice == "2":
                self._remove_item(menu)
            elif choice == "3":
                self._update_price(menu)
            elif choice == "4":
                display_menu(menu)
            elif choice == "5":
                save_menu_to_file(menu)
            elif choice == "6":
                break
            else:
                print("  Invalid choice. Try again.")

    def _add_item(self, menu: list[MenuItem]):
        try:
            name = input("  Item name: ").strip()
            if any(m.get_name().lower() == name.lower() for m in menu):
                print(f"  Item '{name}' already exists.")
                return
            price = float(input("  Price (Rs.): "))
            print(f"  Categories: {', '.join(VALID_CATEGORIES)}")
            category = input("  Category: ").strip()
            item = MenuItem(name, price, category)
            menu.append(item)
            print(f"  '{name}' added successfully.")
        except ValueError as e:
            print(f"  Error: {e}")

    def _remove_item(self, menu: list[MenuItem]):
        name = input("  Item name to remove: ").strip()
        for i, item in enumerate(menu):
            if item.get_name().lower() == name.lower():
                menu.pop(i)
                print(f"  '{name}' removed from menu.")
                return
        print(f"  Item '{name}' not found.")

    def _update_price(self, menu: list[MenuItem]):
        name = input("  Item name to update: ").strip()
        for item in menu:
            if item.get_name().lower() == name.lower():
                try:
                    new_price = float(input(f"  New price for '{name}' (Rs.): "))
                    item.set_price(new_price)
                    print(f"  Price updated to Rs.{new_price:.2f}.")
                except ValueError as e:
                    print(f"  Error: {e}")
                return
        print(f"  Item '{name}' not found.")

    def __str__(self):
        return f"Staff: {self._name} (@{self.__username})"


def display_menu(menu: list[MenuItem]):
    if not menu:
        print("  Menu is empty.")
        return
    print("\n" + "=" * 40)
    print("         Smart Cafe - Full Menu")
    print("=" * 40)
    for category in VALID_CATEGORIES:
        items = [m for m in menu if m.get_category() == category]
        if items:
            print(f"\n  [ {category} ]")
            print("  " + "-" * 36)
            for item in items:
                item.display()
    print("=" * 40)


def save_menu_to_file(menu: list[MenuItem]):
    try:
        os.makedirs(os.path.dirname(MENU_FILE), exist_ok=True)
        with open(MENU_FILE, "w") as f:
            for item in menu:
                f.write(item.to_file_string() + "\n")
        print(f"  Menu saved to file successfully.")
    except IOError as e:
        print(f"  File error: {e}")


def load_menu_from_file() -> list[MenuItem]:
    menu = []
    if not os.path.exists(MENU_FILE):
        return menu
    try:
        with open(MENU_FILE, "r") as f:
            for line in f:
                if line.strip():
                    try:
                        menu.append(MenuItem.from_file_string(line))
                    except ValueError as e:
                        print(f"  Skipping invalid line: {e}")
        print(f"  Menu loaded from file ({len(menu)} items).")
    except IOError as e:
        print(f"  File error loading menu: {e}")
    return menu
