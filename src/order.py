from datetime import datetime
from menu_item import MenuItem

TAX_RATE = 0.05


class Order:
    _order_counter = 1

    def __init__(self):
        self.__order_id = Order._order_counter
        Order._order_counter += 1
        self.__items: list[MenuItem] = []
        self.__quantities: list[int] = []
        self.__timestamp = datetime.now()

    def get_order_id(self) -> int:
        return self.__order_id

    def get_timestamp(self) -> datetime:
        return self.__timestamp

    def add_item(self, item: MenuItem, qty: int):
        if qty <= 0:
            raise ValueError("Quantity must be at least 1.")
        for i, existing in enumerate(self.__items):
            if existing.get_name().lower() == item.get_name().lower():
                self.__quantities[i] += qty
                return
        self.__items.append(item)
        self.__quantities.append(qty)

    def remove_item(self, item_name: str):
        for i, item in enumerate(self.__items):
            if item.get_name().lower() == item_name.lower():
                self.__items.pop(i)
                self.__quantities.pop(i)
                print(f"  '{item_name}' removed from order.")
                return
        raise ValueError(f"Item '{item_name}' not found in this order.")

    def calculate_subtotal(self) -> float:
        return sum(
            self.__items[i].get_price() * self.__quantities[i]
            for i in range(len(self.__items))
        )

    def calculate_total(self, discount: float = 0.0) -> float:
        subtotal = self.calculate_subtotal()
        discounted = subtotal * (1 - discount)
        tax = discounted * TAX_RATE
        return discounted + tax

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def display_receipt(self, customer_name: str = "Guest", discount: float = 0.0) -> str:
        if self.is_empty():
            raise RuntimeError("Order is empty! Cannot generate receipt.")

        subtotal = self.calculate_subtotal()
        discount_amount = subtotal * discount
        discounted_subtotal = subtotal - discount_amount
        tax = discounted_subtotal * TAX_RATE
        total = discounted_subtotal + tax

        lines = []
        lines.append("\n" + "=" * 40)
        lines.append("       ------ Smart Cafe ------")
        lines.append("=" * 40)
        lines.append(f"  Order ID : #{self.__order_id}")
        lines.append(f"  Customer : {customer_name}")
        lines.append(f"  Date     : {self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-" * 40)
        lines.append(f"  {'Item':<18} {'Qty':>4}  {'Price':>8}")
        lines.append("-" * 40)

        for i, item in enumerate(self.__items):
            line_total = item.get_price() * self.__quantities[i]
            lines.append(f"  {item.get_name():<18} {self.__quantities[i]:>4}  Rs.{line_total:>6.2f}")

        lines.append("-" * 40)
        lines.append(f"  {'Subtotal:':<28} Rs.{subtotal:>6.2f}")
        if discount > 0:
            lines.append(f"  {'Discount (' + str(int(discount*100)) + '%):' :<28} Rs.{discount_amount:>6.2f}")
        lines.append(f"  {'Tax (5%):':<28} Rs.{tax:>6.2f}")
        lines.append(f"  {'TOTAL:':<28} Rs.{total:>6.2f}")
        lines.append("=" * 40)
        lines.append("    Thank you for visiting Smart Cafe!")
        lines.append("=" * 40 + "\n")

        receipt = "\n".join(lines)
        return receipt

    def to_file_string(self, customer_name: str) -> str:
        lines = [f"ORDER_ID:{self.__order_id}|CUSTOMER:{customer_name}|DATE:{self.__timestamp}"]
        for i, item in enumerate(self.__items):
            lines.append(f"  {item.get_name()},{self.__quantities[i]},{item.get_price()}")
        lines.append(f"TOTAL:{self.calculate_total():.2f}")
        lines.append("---")
        return "\n".join(lines)
