class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"{self.quantity}x {self.name} @ {self.price}")

    def update_quantity(self, quantity):
        self.quantity = quantity
