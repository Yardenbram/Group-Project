def display_menu():
    print("\n--- Shopping List Manager ---")
    print("1. Show List")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Quit")


def add_item(shopping_list, item):
    """Add item to the list if it's not already there."""
    if item == "":
        print("You can't add a blank item.")
    elif item in shopping_list:
        print(f"'{item}' is already in the list.")
    else:
        shopping_list.append(item)
        print(f"Added '{item}' to the list.")


def remove_item(shopping_list, item):
    """Remove item if it exists in the list."""
    if item == "":
        print("You must enter an item name.")
    elif item in shopping_list:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the list.")
    else:
        print(f"'{item}' not found in the list.")


def show_list(shopping_list):
    """Display the shopping list or a message if it's empty."""
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("\nYour shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")


def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_list(shopping_list)

        elif choice == "2":
            item = input("Enter item to add: ").strip()
            add_item(shopping_list, item)

        elif choice == "3":
            item = input("Enter item to remove: ").strip()
            remove_item(shopping_list, item)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3 or 4.")


if __name__ == "__main__":
    main()
