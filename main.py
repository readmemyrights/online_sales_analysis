from product import Product
from product_manager import ProductManager

manager = ProductManager([
    Product("Dumb phone", 350, 3),
    Product("curved screen tv", 1500, 1)
    ])
manager.add_product(Product("Finnie certified home fluffpile kit", 499, 20))

manager.show_products()
manager.show_total()
