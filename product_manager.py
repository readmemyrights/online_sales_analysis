class ProductManager():
    def __init__(self, products):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            product.show_info()

    def show_total(self):
        total = sum(map(lambda p: p.price * p.quantity, self.products))
        print(f"Total worth of inventory: {total}")
    
    def remove_product(self, name):
        for i in range(len(self.products)):
            if self.products[i].name == name:
                return self.products.pop(i)
