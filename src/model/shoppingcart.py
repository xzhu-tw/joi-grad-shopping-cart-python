from src.model.product import Product
from src.model.customer import Customer
from src.model.order import Order


class ShoppingCart:
    def __init__(self, customer=Customer, products=[]):
        self.products = products
        self.customer = customer

    def add_product(self, product):
        self.products.append(product)

    def checkout(self):
        total_price = 0.00
        loyalty_points_earned = 0.00
        discount_50_per_100_price = 0.00

        for product in self.products:
            discount = 0.00
            if product.product_code.startswith("DISCOUNT_50_PER_100"):
                loyalty_points_earned += (product.price / 5)
                discount_50_per_100_price += product.price
            elif product.product_code.startswith("DIS_10"):
                loyalty_points_earned += (product.price / 10)
                discount += product.price * 0.1
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += (product.price / 15)
                discount += product.price * 0.15
            elif product.product_code.startswith("DIS_20"):
                loyalty_points_earned += (product.price / 20)
                discount += product.price * 0.20
            else:
                loyalty_points_earned += (product.price / 5)

            total_price += product.price - discount

        discount_50_per_100 = int(discount_50_per_100_price / 100) * 50
        total_price -= discount_50_per_100

        return Order(int(loyalty_points_earned), total_price)


    def __str__(self):
        product_list = "".join('%s'%product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
