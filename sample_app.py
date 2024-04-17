from src.model.product import Product
from src.model.customer import Customer
from src.model.shoppingcart import ShoppingCart


def main():
    product1 = Product(10.0, "DIS_10_PRODUCT1", "product 1")
    product2 = Product(20.0, "DIS_10_PRODUCT2", "product 2")

    products = [product1, product2]

    customer = Customer("A Customer")

    shopping_cart = ShoppingCart(customer, products)

    product3 = Product(30.0, "DIS_10_PRODUCT3", "product 3")

    shopping_cart.add_product(product3)

    for _ in range(8):
        product4 = Product(25.0, "DISCOUNT_50_PER_100_4", "product 4")
        shopping_cart.add_product(product4)

    for _ in range(2):
        product5 = Product(70.0, "DISCOUNT_50_PER_100_5", "product 5")
        shopping_cart.add_product(product5)

    print(shopping_cart)

    order = shopping_cart.checkout()

    print(order)


if __name__ == "__main__":
    main()
