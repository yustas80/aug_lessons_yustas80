

class Product:
    def __init__(self, prod_name, description, price=None):
        self.prod_name = prod_name
        self.description = description
        self.price = float(price)

    def __str__(self):
        return f'{self.prod_name} {self.price:.2f}'


class Cart:

    def __init__(self):
        self.usr_cart = {}

    def add_product(self, product, quantity):
        calc = 0
        self.usr_cart[product.prod_name] = quantity
        calc += product.price * self.usr_cart[product.prod_name]
        return f'product {product.prod_name} in quantity {quantity} = {calc}'

    def __str__(self):
        return self.add_product()

    product_1 = Product('apple', 'big', 24)
    product_2 = Product('orange', 'big', 48)
    product_3 = Product('cucumber', 'long', 34.55)
    product_4 = Product('cherry', 'many', 42.15)

    # def cart_calc(self, usr_cart):
    #     summa = self.usr_cart[pro]

    # def __str__(self):

    # def add_prod(self, product: Product):
    #     if isinstance(product, Product):
    #         self.usr_cart.append(product)

    # def cart_price(self, ):

    # def __str__(self):
    #     return f'{self.prod_name} {self.quan} {self.price:.2f}'


print(product_1)
print(Cart().add_product(product_2, 4))
print(Cart().add_product(product_1, 3))

# usr_cart_1 = Cart('Your cart')
# usr_cart_1.usr_cart.append(product_1)
# usr_cart_1.usr_cart.append(product_2)
# usr_cart_1.usr_cart.append(product_3)
