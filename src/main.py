import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from menu_item import MenuItem
from order import Order
from customer import Customer
from staff import Staff, display_menu, save_menu_to_file, load_menu_from_file
from menu_manager import search_and_filter_menu, find_item

ORDERS_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "orders.txt")

DEFAULT_MENU = [
    MenuItem("Coffee", 3.50, "Drinks"),
    MenuItem("Green Tea", 2.00, "Drinks"),
    MenuItem("Cold Brew", 4.50, "Drinks"),
    MenuItem("Mango Smoothie", 5.00, "Drinks"),
    MenuItem("Burger", 8.00, "Fast Food"),
    MenuItem("Club Sandwich", 6.50, "Fast Food"),
    MenuItem("French Fries", 3.00, "Fast Food"),
    MenuItem("Chicken Wrap", 7.00, "Fast Food"),
    MenuItem("Chocolate Cake", 4.00, "Desserts"),
    MenuItem("Brownie", 3.50, "Desserts"),
    MenuItem("Ice Cream", 2.50, "Desserts"),
]

STAFF_ACCOUNTS = [
    Staff("Admin", "admin", "admin123"),
    Staff("Samreen", "samreen", "staff456"),
]


def save_receipt_to_file(receipt: str):
    try:
        os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True)
        with open(ORDERS_FILE, "a") as f:
            f.write(receipt + "\n")
    except IOError as e:
        print(f"  Warning: Could not save receipt to file: {e}")


def login_staff() -> Staff | None:
    print("\n  --- Staff Login ---")
    username = input("  Username: ").strip()
    password = input("  Password: ").strip()
    for staff in STAFF_ACCOUNTS:
        if staff.get_username() == username and staff.authenticate(password):
            print(f"  Welcome, {staff.get_name()}!")
            return staff
    print("  Invalid credentials.")
    return None


def customer_menu(customer: Customer, menu: list[MenuItem]):
    while True:
        print(f"\n  +====== Customer Menu [{customer.get_name()}] ======+")
        if customer.is_student():
            print(f"  | Student discount (10%) applied!            |")
        print(f"  | Customer ID: {customer.get_customer_id():<30}|")
        print("  +--------------------------------------------+")
        print("  | 1. View Menu                               |")
        print("  | 2. Search / Filter Menu                    |")
        print("  | 3. Start New Order                         |")
        print("  | 4. Add Item to Current Order               |")
        print("  | 5. Remove Item from Current Order          |")
        print("  | 6. View Current Order                      |")
        print("  | 7. Checkout (Place Order)                  |")
        print("  | 8. View Order History                      |")
        print("  | 9. Back to Main Menu                       |")
        print("  +--------------------------------------------+")

        choice = input("  Select option: ").strip()

        if choice == "1":
            display_menu(menu)

        elif choice == "2":
            search_and_filter_menu(menu)

        elif choice == "3":
            customer.start_new_order()

        elif choice == "4":
            if customer.get_current_order() is None:
                print("  No active order. Please start a new order first (option 3).")
                continue
            display_menu(menu)
            name = input("  Item name to add: ").strip()
            item = find_item(menu, name)
            if item is None:
                print(f"  Item '{name}' not found in menu.")
                continue
            try:
                qty = int(input("  Quantity: "))
                customer.get_current_order().add_item(item, qty)
                print(f"  {qty}x '{item.get_name()}' added to order.")
            except ValueError as e:
                print(f"  Error: {e}")

        elif choice == "5":
            if customer.get_current_order() is None or customer.get_current_order().is_empty():
                print("  No active order or order is empty.")
                continue
            name = input("  Item name to remove: ").strip()
            try:
                customer.get_current_order().remove_item(name)
            except ValueError as e:
                print(f"  Error: {e}")

        elif choice == "6":
            order = customer.get_current_order()
            if order is None or order.is_empty():
                print("  No items in current order.")
            else:
                try:
                    print(order.display_receipt(customer.get_name(), customer.get_discount()))
                except RuntimeError as e:
                    print(f"  {e}")

        elif choice == "7":
            try:
                receipt = customer.place_order()
                print(receipt)
                save_receipt_to_file(receipt)
                print("  Receipt saved to orders.txt")
            except RuntimeError as e:
                print(f"  Error: {e}")

        elif choice == "8":
            customer.view_order_history()

        elif choice == "9":
            break
        else:
            print("  Invalid option. Try again.")


def main():
    print("\n" + "=" * 50)
    print("       Welcome to Smart Cafe System")
    print("       Department of Software Engineering")
    print("=" * 50)

    menu = load_menu_from_file()
    if not menu:
        print("  No saved menu found. Loading default menu...")
        menu = list(DEFAULT_MENU)
        save_menu_to_file(menu)

    while True:
        print("\n  +======= Main Menu =======+")
        print("  | 1. Customer Login        |")
        print("  | 2. Staff / Admin Login   |")
        print("  | 3. Exit                  |")
        print("  +==========================+")
        choice = input("  Select: ").strip()

        if choice == "1":
            name = input("  Enter your name: ").strip()
            if not name:
                print("  Name cannot be empty.")
                continue
            student_input = input("  Are you a student? (y/n): ").strip().lower()
            is_student = student_input == "y"
            customer = Customer(name, is_student)
            print(f"\n  {customer}")
            customer_menu(customer, menu)

        elif choice == "2":
            staff = login_staff()
            if staff:
                staff.manage_menu(menu)

        elif choice == "3":
            save_menu_to_file(menu)
            print("\n  Thank you for using Smart Cafe System. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  Interrupted. Exiting Smart Cafe. Goodbye!")
