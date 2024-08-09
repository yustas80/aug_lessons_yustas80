class Product:
    """
    Class for product representation.
    """

    def __init__(self, name: str, price: int | float, currency='UAH'):
        self.name = name
        self.price = price
        self.currency = currency

    def __str__(self):
        return f'{self.name}: {self.price:.2f} {self.currency}'


class Cart:
    """
    Class for cart representation.
    """

    def __init__(self):
        self.__products = {}

    def add_product(self, product: Product, quantity: int | float = 1):
        self.__products[product] = self.__products.get(product, 0) + quantity

    def total(self):
        return sum(product.price * quantity for product, quantity in self.__products.items())

    def __str__(self):
        return '\n'.join([f'{product} x {quantity} = {product.price * quantity} {product.currency}'
                          for product, quantity in self.__products.items()])


if __name__ == '__main__':
    cart = Cart()
    cart.add_product(Product('Bread', 10), 5)
    cart.add_product(Product('Milk', 20),2)
    cart.add_product(Product('Butter', 30), 4)
    print(cart)
    print(f'Total: {cart.total()} UAH')
