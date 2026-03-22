class Cart():
    def __init__(self, cart_items):
        self.cart_items = cart_items

    def add_item(self, item):
        self.cart_items.append(item)

    def show_items(self):
        for item in self.cart_items:
            item.show_info()

    def show_total(self):
        total = sum(map(lambda p: p.price * p.quantity, self.cart_items))
        print(f"Total worth of cart: {total}")
