#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}.\n"
        else:
            return "There is no discount to apply.\n"

    def void_last_transaction(self):
        if self.items:
            last_item_price = self._get_last_item_price()
            self.total -= last_item_price
            self.items.pop()
        else:
            return "No transactions to void."

    def _get_last_item_price(self):
        last_item_title = self.items[-1]
        return self._get_price_of_item(last_item_title)

