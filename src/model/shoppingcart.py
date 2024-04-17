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
        total_before_discount = sum(p.price for p in self.products)
        #print("total_before_discount is:", total_before_discount)
        total_price = 0.00
        loyalty_points_earned = 0.00

        discount_50_per_100_products_price = sum(p.price for p in self.products if p.product_code.startswith("DISCOUNT_50_PER_100"))
        #print("discount_50_per_100_products_price is ", discount_50_per_100_products_price)
        discount_50_per_100 = int(discount_50_per_100_products_price / 100) * 50
        #print("discount_50_per_100 is ", discount_50_per_100)

        for product in self.products:
            if product.product_code.startswith("DISCOUNT_50_PER_100"):
                loyalty_points_earned += (product.price / 5)
                total_price += product.price
                #print("total price by add DISCOUNT_50_PER_100 is ", total_price)
            elif product.product_code.startswith("DIS_10"):
                loyalty_points_earned += (product.price / 10)
                total_price += product.price * 0.9
                #print("total price by add DIS_10 is ", total_price)
            elif product.product_code.startswith("DIS_15"):
                loyalty_points_earned += (product.price / 15)
                total_price += product.price * 0.85
                #print("total price by add DIS_15 is ", total_price)
            elif product.product_code.startswith("DIS_20"):
                loyalty_points_earned += (product.price / 20)
                total_price += product.price * 0.8
                #print("total price by add DIS_20 is ", total_price)
            else:
                loyalty_points_earned += (product.price / 5)
                total_price += product.price
                #print("total price by add no_discount is ", total_price)

        total_price -= discount_50_per_100
        #print("total price minus discount_50_per_100 as: ", total_price)

        additional_discount = 0.0
        if total_price > 500:
            additional_discount = total_price * 0.05  # 5%的额外折扣
            total_price -= additional_discount

        total_after_discount = total_price
        #print("after check 0.05 additional_discount, total_after_price is ", total_after_discount)
        total_discount = total_before_discount - total_after_discount
        #print("total_discount is ", total_discount)

        return Order(int(loyalty_points_earned), total_before_discount, total_discount, total_after_discount)


    def __str__(self):
        product_list = "".join('%s'%product for product in self.products)
        return "Customer: %s \nBought: \n%s" % (self.customer, product_list)
