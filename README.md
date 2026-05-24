# Smart Cafe Ordering System

A Python-based cafe management system developed as a semester project for the Software Construction and Development Lab (5th Semester).

**Instructor:** Ms. Samreen  
**Course:** Software Construction and Development Lab

---

## Features

### Core Features
- **Dynamic Menu Management** — Add, remove, update items categorized as Drinks, Fast Food, or Desserts
- **Order System** — Multiple items per order with quantity support, remove items, real-time totals
- **Billing System** — Formatted receipt with subtotal, 5% tax, and total
- **Customer Management** — Unique customer IDs, multiple orders, order history
- **Staff/Admin Role** — Secure login with menu management access
- **File Handling** — Menu persisted in `data/menu.txt`, receipts saved to `data/orders.txt`
- **Exception Handling** — Invalid input, empty order checkout, file errors
- **Search & Filter** — Search items by name, filter by category

### Bonus Features
- **Discount System** — 10% discount for student customers
- **Login System** — Username/password authentication for staff

---

## Project Structure

```
SmartCafe/
├── src/
│   ├── main.py          # Entry point, main menu loop
│   ├── person.py        # Base Person class
│   ├── menu_item.py     # MenuItem class with file serialization
│   ├── order.py         # Order class with billing logic
│   ├── customer.py      # Customer class (inherits Person)
│   ├── staff.py         # Staff class (inherits Person) + file helpers
│   └── menu_manager.py  # Search & filter utilities
├── data/
│   ├── menu.txt         # Persisted menu items
│   └── orders.txt       # Saved order receipts
├── build/
├── README.md
└── .gitignore
```

---

## How to Run

```bash
cd SmartCafe/src
python main.py
```

Requires **Python 3.10+** (uses union type hints).

---

## Staff Login Credentials

| Username | Password  |
|----------|-----------|
| admin    | admin123  |
| samreen  | staff456  |

---

## OOP Concepts Used

| Concept         | Where Applied                                      |
|-----------------|----------------------------------------------------|
| Inheritance     | `Customer` and `Staff` both inherit from `Person`  |
| Encapsulation   | Private attributes with getters/setters            |
| Composition     | `Customer` has a list of `Order` objects           |
| Exception Handling | `try/except` across all user input and file I/O |
| File I/O        | `menu.txt` and `orders.txt` for persistence        |

---

## Sample Receipt

```
========================================
       ------ Smart Cafe ------
========================================
  Order ID : #1
  Customer : Ali
  Date     : 2026-05-24 10:30:00
----------------------------------------
  Item               Qty     Price
----------------------------------------
  Coffee               2  Rs.  7.00
  Brownie              1  Rs.  3.50
----------------------------------------
  Subtotal:                Rs. 10.50
  Tax (5%):                Rs.  0.53
  TOTAL:                   Rs. 11.03
========================================
    Thank you for visiting Smart Cafe!
========================================
```
