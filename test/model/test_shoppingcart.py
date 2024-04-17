import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"


class ShoppingCartTest(unittest.TestCase):
    def test_checkout_total_over_500(self):
        product1 = Product(10.0, "DIS_10_PRODUCT1", "product 1")
        product2 = Product(20.0, "DIS_10_PRODUCT2", "product 2")
        products = [product1, product2]
        customer = Customer("A Customer")
        shopping_cart = ShoppingCart(customer, products)
        product3 = Product(30.0, "DIS_10_PRODUCT3", "product 3")
        shopping_cart.add_product(product3)

        product4 = Product(30.0, "DIS_15_A", "product 3")
        shopping_cart.add_product(product4)
        product5 = Product(50.0, "DIS_20_A", "product 5")
        shopping_cart.add_product(product5)

        product6 = Product(150.0, "DISCOUNT_50_PER_100_A", "product6")
        shopping_cart.add_product(product6)
        product7 = Product(300.0, "", "product 7")
        shopping_cart.add_product(product7)
        for _ in range(2):
                product8 = Product(70.0, "DISCOUNT_50_PER_100_B", "product 8")
                shopping_cart.add_product(product8)
        order = shopping_cart.checkout()
        self.assertAlmostEqual(order.total_after_discount, 579.02, places=2)
        self.assertAlmostEqual(order.total_before_discount, 730, places=2)
        self.assertAlmostEqual(order.total_discount, 150.98, places=2)
        self.assertAlmostEqual(order.loyalty_points_earned, 128, places=2)
