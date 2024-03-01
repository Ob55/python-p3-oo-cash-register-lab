#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []  # Holds item names for simplicity
        self.transactions = []  # Keeps track of each transaction as a tuple (price, quantity)

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)  # Add item names, considering quantity
        self.transactions.append((price, quantity))  # Record transaction

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}."
        else:
            return "Sorry, there is no discount to apply."

    def void_last_transaction(self):
        if self.transactions:
            last_price, last_quantity = self.transactions.pop()
            self.total -= last_price * last_quantity
            # Assume each transaction adds unique items, for simplicity
            for _ in range(last_quantity):
                self.items.pop()  # Remove the last item(s) added
        else:
            self.total = 0  # Reset total if no transactions left

# Example usage and testing
if __name__ == "__main__":
    register = CashRegister(discount=20)
    register.add_item("apple", 100, 5)  # Adding 5 apples at $100 each
    print(register.total)  # Expect 500
    print(register.apply_discount())  # Applying a 20% discount
    register.void_last_transaction()  # Removing the last transaction
    print(register.total)  # Updated total after voiding the last transaction
    print(register.items)  # Should reflect removed items
