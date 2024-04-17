import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"


class ShoppingCartTest(unittest.TestCase):
    def test_should_calculate_price_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(100.00, order.total)

    def test_should_calculate_loyalty_points_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(20, order.loyalty_points)

    def test_should_calculate_price_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(90.00, order.total)

    def test_should_calculate_loyalty_points_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)

    def test_should_calculate_price_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(85.00, order.total)

    def test_should_calculate_loyalty_points_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(6, order.loyalty_points)

    def test_should_calculate_loyalty_points_with_20_percent_discount(self):
         products = [Product(PRICE, "DIS_20_ABCD", PRODUCT)]
         cart = ShoppingCart(CUSTOMER, products)

         order = cart.checkout()

         self.assertEqual(5, order.loyalty_points)

    def test_no_discount_under_100(self):
        products = [Product(90, "DISCOUNT_50_PER_100_A", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(90, order.total)

    def test_discount_between_100_to_200(self):
        products = [Product(20, "DISCOUNT_50_PER_100_A", PRODUCT)] * 8
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(110, order.total)

    def test_discount_between_200_to_300(self):
        products = [Product(20, "DISCOUNT_50_PER_100_A", PRODUCT)] * 11
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(120, order.total)

    def test_no_discount_when_different_product_codes(self):
        products = [Product(30, "DISCOUNT_50_PER_100_A", "T1"), Product(40, "DISCOUNT_50_PER_100_B", "T2")]
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(70, order.total)

    def test_discount_for_different_product_codes(self):
        products = [Product(70, "DISCOUNT_50_PER_100_A", "T1"), Product(60, "DISCOUNT_50_PER_100_B", "T2")]
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(80, order.total)

    def test_discount_for_different_product_codes(self):
        products = [Product(110, "DISCOUNT_50_PER_100_A", "T1"), Product(120, "DISCOUNT_50_PER_100_B", "T2")]
        cart = ShoppingCart(CUSTOMER, products)
        order = cart.checkout()
        self.assertEqual(130, order.total)