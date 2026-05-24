from person import Person
from order import Order

STUDENT_DISCOUNT = 0.10


class Customer(Person):
    _id_counter = 1001

    def __init__(self, name: str, is_student: bool = False):
        super().__init__(name)
        self.__customer_id = Customer._id_counter
        Customer._id_counter += 1
        self.__orders: list[Order] = []
        self.__is_student = is_student
        self.__current_order: Order | None = None

    def get_customer_id(self) -> int:
        return self.__customer_id

    def is_student(self) -> bool:
        return self.__is_student

    def get_discount(self) -> float:
        return STUDENT_DISCOUNT if self.__is_student else 0.0

    def start_new_order(self):
        self.__current_order = Order()
        print(f"  New order #{self.__current_order.get_order_id()} started for {self._name}.")

    def get_current_order(self) -> Order | None:
        return self.__current_order

    def place_order(self) -> str:
        if self.__current_order is None or self.__current_order.is_empty():
            raise RuntimeError("Order is empty! Add items before placing.")
        receipt = self.__current_order.display_receipt(self._name, self.get_discount())
        self.__orders.append(self.__current_order)
        self.__current_order = None
        return receipt

    def view_order_history(self):
        if not self.__orders:
            print(f"  No order history for {self._name}.")
            return
        print(f"\n  Order history for {self._name} (ID: {self.__customer_id}):")
        print(f"  Total orders placed: {len(self.__orders)}")
        for order in self.__orders:
            print(f"    - Order #{order.get_order_id()} on {order.get_timestamp().strftime('%Y-%m-%d %H:%M:%S')}"
                  f"  |  Total: Rs.{order.calculate_total(self.get_discount()):.2f}")

    def get_orders(self) -> list[Order]:
        return self.__orders

    def __str__(self):
        label = " [Student]" if self.__is_student else ""
        return f"Customer: {self._name}{label} (ID: {self.__customer_id})"
