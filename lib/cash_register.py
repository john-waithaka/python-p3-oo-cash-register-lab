#!/usr/bin/env python3

# class CashRegister:
#   pass


class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(item)
        self.previous_transactions.append(
            {"item": item, "quantity": quantity, "price": price}
        )

    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        self.total -= (
            self.previous_transactions[-1]["price"]
            * self.previous_transactions[-1]["quantity"]
        )
        for _ in range(self.previous_transactions[-1]["quantity"]):
            self.items.pop()
        self.previous_transactions.pop()



#improved code but not passing
# class CashRegister:
#     def __init__(self, discount=0.0):
#         self.discount_rate = discount / 100  # Store discount as a decimal (0.0 to 1.0)
#         self.total = 0.0  # Use float for accurate price calculations
#         self.items = []
#         self.previous_transactions = []

#     def add_item(self, item, price, quantity=1):
#         if not isinstance(price, (int, float)) or price <= 0:
#             raise ValueError("Price must be a positive number.")
#         if not isinstance(quantity, int) or quantity <= 0:
#             raise ValueError("Quantity must be a positive integer.")

#         self.total += price * quantity
#         self.items.extend([item] * quantity)  # Efficient list extension
#         self.previous_transactions.append(
#             {"item": item, "quantity": quantity, "price": price}
#         )

#     def apply_discount(self):
#         if self.discount_rate > 0:
#             discount_amount = self.total * self.discount_rate
#             self.total -= discount_amount
#             print(f"After the discount of {self.discount_rate * 100}%, the total comes to ${self.total:.2f}.")  # Format total with 2 decimal places
#         else:
#             print("There is no discount to apply.")

#     def void_last_transaction(self):
#         if not self.previous_transactions:
#             return "There are no transactions to void."
#         last_transaction = self.previous_transactions.pop()
#         self.total -= last_transaction["price"] * last_transaction["quantity"]
#         self.items = self.items[:- last_transaction["quantity"]]  # Efficient item removal

#this code helps to take care of
#''' 
# Improvements:
  # Discount Rate: The discount is stored as a decimal (0.0 to 1.0) for accurate calculations.
  # Floating-Point Arithmetic: All price calculations use float to avoid rounding errors.
  # Error Handling: The add_item method checks for valid price and quantity types, raising ValueError with informative messages for invalid input.
  # List Extensions: The add_item method uses extend for efficient item appending.
  # Discount Message: The apply_discount method formats the discount percentage and total with two decimal places for better readability.
  # Item Removal: The void_last_transaction method uses slicing to efficiently remove the last transaction's items from the items list.
#'''