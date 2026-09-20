class Coffee:

    # Classes are basically blueprints.
    # For this Coffee class, every coffee object needs a name and a price.
    # For example:
    # latte = Coffee("Latte", 3.00)
    # That object will remember its own name and price.
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:

    # Initialize every new order with an empty list.
    # The list will store the Coffee objects that the user adds.
    def __init__(self):
        self.items = []

    # Add a coffee object to the order.
    def add_item(self, coffee):
        self.items.append(coffee)
        print(f"Added {coffee.name} to your order!")

    # Delete an item from the user's cart.
    def delete_item(self):

        if not self.items:
            print("Your cart is empty. Nothing to delete!")
            return

        print("\nWhich item in your cart would you like to delete?")

        # enumerate gives each item a number starting at 1.
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        choice = input("Choose the item number to delete: ").strip()

        # Make sure the user entered a number that actually exists in the cart.
        if choice.isdigit() and 1 <= int(choice) <= len(self.items):

            # Lists start at index 0, so subtract 1 from the user's choice.
            removed_item = self.items.pop(int(choice) - 1)

            print(f"Removed {removed_item.name} from your order.")

        else:
            print("Invalid item number.")

    # Calculate and return the total price of everything in the order.
    def total(self):
        return sum(item.price for item in self.items)

    # Display everything currently inside the order.
    def show_order_summary(self):

        if not self.items:
            print("No items in order.")
            return

        print("\n--- Your Order ---")

        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item.name} - ${item.price:.2f}")

        print(f"Total: ${self.total():.2f}")

    # Handle the checkout process.
    def checkout(self):

        if not self.items:
            print("Your cart is empty.")
            return False

        self.show_order_summary()

        confirm = input(
            "\nProceed to checkout? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            print("Order confirmed! Thank you.")

            # Clear the cart after the order is completed.
            self.items.clear()

            return True

        else:
            print("Checkout cancelled.")
            return False


# Display options after the user has added something to the cart.
def order_options(order):

    while True:

        print("\nWhat would you like to do next?")
        print("1. Add More Coffee")
        print("2. View Order")
        print("3. Delete From Cart")
        print("4. Checkout")

        choice = input("Pick a number to continue: ").strip()

        if choice == "1":
            # Return to the main coffee menu.
            return False

        elif choice == "2":
            order.show_order_summary()

        elif choice == "3":
            order.delete_item()

        elif choice == "4":

            if order.checkout():
                return True

        else:
            print("Invalid choice. Please try again.")


# Display the coffee menu and handle user input.
def main():

    menu = [
        Coffee("Espresso", 2.50),
        Coffee("Caramel Latte", 5.00),
        Coffee("Latte", 3.00),
        Coffee("Mocha", 1.50),
        Coffee("Caramel Frappuccino", 4.75)
    ]

    # Create one Order object to hold the user's cart.
    order = Order()

    while True:

        print("\n--- Coffee Menu ---")

        for i, coffee in enumerate(menu, 1):
            print(f"{i}. {coffee.name} - ${coffee.price:.2f}")

        print("6. View Order")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Choose an option: ").strip()

        # Options 1-5 represent coffees from the menu.
        if choice in ["1", "2", "3", "4", "5"]:

            # Convert the user's choice into the correct list index.
            order.add_item(menu[int(choice) - 1])

            finished = order_options(order)

            if finished:
                return

        elif choice == "6":

            order.show_order_summary()

            # Only show the cart options if there is something in the cart.
            if order.items:

                finished = order_options(order)

                if finished:
                    return

        elif choice == "7":

            if order.checkout():
                return

        elif choice == "8":

            print("Thanks for visiting! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again!")


# Only automatically run the program when this file itself is executed.
if __name__ == "__main__":
    main()