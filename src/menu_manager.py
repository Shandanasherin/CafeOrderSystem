from menu_item import MenuItem, VALID_CATEGORIES


def search_by_name(menu: list[MenuItem], query: str) -> list[MenuItem]:
    query = query.lower().strip()
    results = [m for m in menu if query in m.get_name().lower()]
    return results


def filter_by_category(menu: list[MenuItem], category: str) -> list[MenuItem]:
    return [m for m in menu if m.get_category().lower() == category.lower()]


def find_item(menu: list[MenuItem], name: str) -> MenuItem | None:
    for item in menu:
        if item.get_name().lower() == name.lower():
            return item
    return None


def search_and_filter_menu(menu: list[MenuItem]):
    print("\n  +---- Search & Filter ----+")
    print("  | 1. Search by name       |")
    print("  | 2. Filter by category   |")
    print("  +-------------------------+")
    choice = input("  Select: ").strip()

    if choice == "1":
        query = input("  Enter search term: ").strip()
        results = search_by_name(menu, query)
        if results:
            print(f"\n  Results for '{query}':")
            print("  " + "-" * 36)
            for item in results:
                item.display()
        else:
            print(f"  No items found matching '{query}'.")

    elif choice == "2":
        print(f"  Categories: {', '.join(VALID_CATEGORIES)}")
        category = input("  Enter category: ").strip()
        results = filter_by_category(menu, category)
        if results:
            print(f"\n  Items in '{category}':")
            print("  " + "-" * 36)
            for item in results:
                item.display()
        else:
            print(f"  No items found in category '{category}'.")
    else:
        print("  Invalid option.")
