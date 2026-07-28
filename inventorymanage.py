inventory = {}
while True:
    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        inventory[product] = {
            "Quantity": quantity,
            "Price": price
        }

        print("Product added successfully!")

    elif choice == "2":
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\n--- Product List ---")
            for product, details in inventory.items():
                print(f"Product: {product}")
                print(f"Quantity: {details['Quantity']}")
                print(f"Price: {details['Price']}")
                print("-" * 25)

    elif choice == "3":
        product = input("Enter product name to update: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            price = float(input("Enter new price: "))

            inventory[product]["Quantity"] = quantity
            inventory[product]["Price"] = price

            print("Product updated successfully!")
        else:
            print("Product not found.")

    elif choice == "4":
        product = input("Enter product name to delete: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found.")

    elif choice == "5":
        print("Thank you for using the Inventory Management System.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")