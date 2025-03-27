class DataValidationError(ValueError):
    """Custom error for invalid data format."""
    pass

class DataNotFound(KeyError):
    """Custom error for data not found."""
    pass

class ProcessingError(Exception):
    """General error during data processing."""
    pass

def validate_data(data_dict):
    """Validates the structure and content of the input dictionary."""
    if not isinstance(data_dict, dict):
        raise DataValidationError("Input must be a dictionary.")

    required_keys = {"items", "users", "settings"}
    if not required_keys.issubset(data_dict.keys()):
        missing_keys = required_keys - set(data_dict.keys())
        raise DataValidationError(f"Missing required keys: {missing_keys}")

    if not isinstance(data_dict["items"], list) or not all(isinstance(item, tuple) and len(item) == 2 for item in data_dict["items"]):
        raise DataValidationError("Items must be a list of tuples (name, price).")

    if not isinstance(data_dict["users"], dict):
        raise DataValidationError("Users must be a dictionary.")

    if not isinstance(data_dict["settings"], dict):
        raise DataValidationError("Settings must be a dictionary")

    return True

def process_data(data_dict, user_id):
    """Processes the data, calculating total price for a user's items."""
    try:
        validate_data(data_dict) #validate input data

        if user_id not in data_dict["users"]:
            raise DataNotFound(f"User ID {user_id} not found.")

        user_items = data_dict["users"][user_id]
        total_price = 0
        item_names = set()

        for item_name in user_items:
            found = False
            for name, price in data_dict["items"]:
                if name == item_name:
                    total_price += price
                    item_names.add(name)
                    found = True
                    break
            if not found:
                print(f"Warning: Item '{item_name}' not found in item list.")

        discount = data_dict["settings"].get("discount", 0) # get discount, default 0.
        if discount > 0:
          total_price = total_price * (1 - discount) #Apply the discount.

        return total_price, item_names

    except DataValidationError as e:
        print(f"Data validation error: {e}")
        return None, None
    except DataNotFound as e:
        print(f"Data not found: {e}")
        return None, None
    except Exception as e:
        raise ProcessingError(f"An unexpected error occurred: {e}")

def add_item(data_dict, item_name, item_price):
    """Adds a new item to the data dictionary."""
    try:
        if not isinstance(item_price, (int, float)):
            raise ValueError("Item price must be a number.")
        data_dict["items"].append((item_name, item_price))
        print(f"Item '{item_name}' added with price ${item_price:.2f}")
    except ValueError as e:
        print(f"Error adding item: {e}")

def update_item_price(data_dict, item_name, new_price):
    """Updates the price of an existing item."""
    try:
        if not isinstance(new_price, (int, float)):
            raise ValueError("New price must be a number.")
        for i, (name, price) in enumerate(data_dict["items"]):
            if name == item_name:
                data_dict["items"][i] = (item_name, new_price)
                print(f"Price of '{item_name}' updated to ${new_price:.2f}")
                return
        raise DataNotFound(f"Item '{item_name}' not found.")
    except (ValueError, DataNotFound) as e:
        print(f"Error updating item price: {e}")

def display_items(data_dict):
    """Displays the current items and their prices."""
    print("\nCurrent Items and Prices:")
    for name, price in data_dict["items"]:
        print(f"- {name}: ${price:.2f}")

def add_user(data_dict, user_id, user_items):
    """Adds a new user to the data dictionary."""
    if user_id in data_dict["users"]:
        print(f"User ID '{user_id}' already exists.")
        return

    for item in user_items:
        found = False
        for name, price in data_dict["items"]:
            if name == item:
                found = True
                break
        if not found:
            try:
                price = float(input(f"Enter price for item '{item}': "))
                data_dict["items"].append((item, price))
                print(f"Item '{item}' added with price ${price:.2f}")
            except ValueError:
                print("Invalid price input. Item not added.")
                return

    data_dict["users"][user_id] = user_items
    print(f"User '{user_id}' added with items: {user_items}")

def update_user_items(data_dict, user_id, new_items):
    """Updates the items associated with an existing user."""
    if user_id not in data_dict["users"]:
        print(f"User ID '{user_id}' not found.")
        return
    data_dict["users"][user_id] = new_items
    print(f"Items for user '{user_id}' updated to: {new_items}")

def display_users(data_dict):
    """Displays the current users and their items."""
    print("\nCurrent Users and Items:")
    for user_id, items in data_dict["users"].items():
        print(f"- {user_id}: {items}")

def main():
    """Main function to demonstrate data processing and user interaction."""
    data = {
        "items": [("apple", 1.0), ("banana", 0.5), ("orange", 0.8)],
        "users": {
            "user123": ["apple", "banana"],
            "user456": ["orange", "apple", "grape"],
        },
        "settings": {"discount": 0.1}
    }

    while True:
        print("\nOptions:")
        print("1. Process user data")
        print("2. Add item")
        print("3. Update item price")
        print("4. Display items")
        print("5. Add user")
        print("6. Update user items")
        print("7. Display users")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_id = input("Enter user ID: ")
            total, items = process_data(data, user_id)

            if total is not None:
                print(f"Total price for user {user_id}: ${total:.2f}")
                print(f"Items purchased: {items}")

        elif choice == "2":
            item_name = input("Enter item name: ")
            try:
                item_price = float(input("Enter item price: "))
                add_item(data, item_name, item_price)
            except ValueError:
                print("Invalid price input.")

        elif choice == "3":
            item_name = input("Enter item name to update: ")
            try:
                new_price = float(input("Enter new price: "))
                update_item_price(data, item_name, new_price)
            except ValueError:
                print("Invalid price input.")

        elif choice == "4":
            display_items(data)

        elif choice == "5":
            user_id = input("Enter user ID: ")
            user_items_str = input("Enter user items (comma-separated): ")
            user_items = [item.strip() for item in user_items_str.split(",")]
            add_user(data, user_id, user_items)

        elif choice == "6":
            user_id = input("Enter user ID to update: ")
            new_items_str = input("Enter new items (comma-separated): ")
            new_items = [item.strip() for item in new_items_str.split(",")]
            update_user_items(data, user_id, new_items)

        elif choice == "7":
            display_users(data)

        elif choice == "8":
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
