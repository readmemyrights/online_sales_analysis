from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager([
    Product("Dumb phone", 350, 3),
    Product("curved screen tv", 1500, 1)
    ])
manager.add_product(Product("Finnie certified home fluffpile kit", 499, 20))
cart = Cart([Product("Dumb phone", 350, 1)])
cart.add_item(Product("Finnie certified home fluffpile kit", 499, 2))

manager.show_products()
manager.show_total()
cart.show_items()
cart.show_total()
