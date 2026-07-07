

# Budget App

This is a Python-based budget tracking application designed to help users manage their finances across different categories (e.g., Food, Clothing, Entertainment).

## Features

* **Ledger Tracking:** Maintain a detailed history of all deposits, withdrawals, and transfers within each category.
* **Balance Management:** Easily check the current balance of any category.
* **Inter-category Transfers:** Move funds seamlessly between different spending categories with automatic ledger logging.
* **Visual Spend Chart:** Generate a text-based bar chart that displays the percentage of total spending per category.

## How It Works

* **`Category` Class:** Each category is an object that keeps track of its own name, ledger, and balance.
* **`deposit` & `withdraw`:** Methods to add or remove funds with optional descriptions.
* **`transfer`:** A method to move money from one category to another, creating entries in both ledgers for auditability.
* **`create_spend_chart`:** A utility function that processes a list of categories and renders a formatted bar chart of total spending.

## Usage Example

```python
# Create categories
food = Category("Food")
clothing = Category("Clothing")

# Perform transactions
food.deposit(1000, "Initial Deposit")
food.withdraw(10.15, "Groceries")
food.transfer(50, clothing)

# View category summary
print(food)

# Generate a spend chart
print(create_spend_chart([food, clothing]))

```

