class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} грн.'


class Customer:

    def __init__(self, name: str, surname: str, phone: str):
        self.name = name
        self.surname = surname
        self.phone = phone

    def __str__(self):
        return f'\t{self.surname} {self.name[0]}., {self.phone}'


class Cart:

    def __init__(self, customer: Customer = None):
        self.customer = customer
        self.products = []
        self.quantities = []

    def add_product(self, product: Product, quantity: int | float):
        if product in self.products:
            index = self.products.index(product)
            self.quantities[index] += quantity
        else:
            self.products.append(product)
            self.quantities.append(quantity)

    def total(self):
        res = 0
        for index, item in enumerate(self.products):
            res += item.price * self.quantities[index]
        return res

    def __str__(self):
        res = f'{self.customer}\n'

        for index, item in enumerate(self.products):
            res += f'{item} x {self.quantities[index]} = {item.price * self.quantities[index]} UAH.\n'

        res += f'Total price: {self.total()} UAH.'

        return res


pr_1 = Product('banana', 10)
pr_2 = Product('apple', 20)


customer_1 = Customer('Keian',  'Roman1',  '1535853')
customer_2 = Customer('Keian ',  'Roman2',  '1585358')

order_1 = Cart(customer_1)
order_2 = Cart(customer_2)

order_1.add_product(pr_1, 1.5)
order_1.add_product(pr_2, 2)

order_2.add_product(pr_1, 2)
order_2.add_product(pr_2, 5)

print(order_1)

print(order_2)
