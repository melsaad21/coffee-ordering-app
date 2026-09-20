# Coffee Ordering Application

A console-based coffee ordering application built with Python.

This project was created to practice object-oriented programming, classes, methods, lists, input validation, and managing application state through a simple ordering system.

## Features

- Displays a menu of coffee options and prices
- Allows users to add multiple coffees to an order
- Stores selected items in a shopping cart
- Displays an order summary
- Calculates the total order price
- Allows users to remove individual items from the cart
- Validates menu and cart selections
- Supports checkout confirmation
- Clears the order after a successful checkout
- Allows users to continue editing their order before checking out

## How It Works

The program uses two main classes:

### Coffee

The `Coffee` class represents an individual coffee item.

Each coffee object stores:

- Name
- Price

Example:

```python
Coffee("Caramel Latte", 5.00)
```

### Order

The `Order` class manages the user's current order.

It is responsible for:

- Adding coffees
- Removing coffees
- Displaying the order
- Calculating the total
- Handling checkout

The user's selected `Coffee` objects are stored inside a list within the `Order` object.

## Menu

The application includes:

- Espresso
- Caramel Latte
- Latte
- Mocha
- Caramel Frappuccino

Users can also:

- View their current order
- Remove items
- Checkout
- Exit the program

## Technologies Used

- Python

## Concepts Practiced

- Object-Oriented Programming
- Classes and objects
- Constructors (`__init__`)
- Instance attributes
- Methods
- Functions
- Lists
- Loops
- Conditional statements
- Input validation
- String formatting
- Program state management

## Running the Project

Make sure Python is installed.

Clone the repository and run:

```bash
python coffee_ordering_app.py
```

## Example

```text
--- Coffee Menu ---
1. Espresso - $2.50
2. Caramel Latte - $5.00
3. Latte - $3.00
4. Mocha - $1.50
5. Caramel Frappuccino - $4.75
6. View Order
7. Checkout
8. Exit

Choose an option: 2
Added Caramel Latte to your order!

What would you like to do next?
1. Add More Coffee
2. View Order
3. Delete From Cart
4. Checkout

Pick a number to continue: 1

--- Coffee Menu ---
1. Espresso - $2.50
2. Caramel Latte - $5.00
3. Latte - $3.00
4. Mocha - $1.50
5. Caramel Frappuccino - $4.75
6. View Order
7. Checkout
8. Exit

Choose an option: 4
Added Mocha to your order!

What would you like to do next?
1. Add More Coffee
2. View Order
3. Delete From Cart
4. Checkout

Pick a number to continue: 2

--- Your Order ---
1. Caramel Latte - $5.00
2. Mocha - $1.50
Total: $6.50
```

## Project Structure

```text
coffee-ordering-app/
├── coffee_ordering_app.py
└── README.md
```

## Purpose

This project helped me strengthen my understanding of object-oriented programming by separating responsibilities between different classes.

The `Coffee` class represents individual menu items, while the `Order` class manages the user's cart, total price, item removal, and checkout process.

It also helped me practice breaking a larger program into smaller methods and functions instead of placing all of the application logic inside one block of code.