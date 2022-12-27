class Item:
    def __init__(self, name: str, price: float, description: str, screen_diag: float):
        self.name = name
        self.price = price
        self.description = description
        self.screen_diag = screen_diag

    def __str__(self):
        return self.name


class User:
    def __init__(self, name: str, surname: str, email: str, numberphone: str, is_subscriber: bool):
        self.name = name
        self.surname = surname
        self.email = email
        self.numberphone = numberphone
        self.is_subscriber = is_subscriber

    def __str__(self):
        return f'{self.name} {self.surname}'


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        self.products[item] = cnt

    def __str__(self):
        buyed_products = ''
        for product, count in self.products.items():
            buyed_products += f'\t{product}: {count} pcs.\n'

        return f'User: {self.user}\n' \
               f'Items:\n' \
               f'{buyed_products}'

    def get_total(self):
        total = 0
        for product, count in self.products.items():
            total += product.price * count
        return f'Total: {total} UAH'


hp17 = Item('hp pavilion', 34000, 'gaming laptop', 17.3)
air_m1 = Item('air M1', 42999, 'business laptop', 13.3)
print(hp17)
print(air_m1)
print()

buyer = User("Petr", "Petrov", "petr@gmail.com", "02628162", True)
print(buyer)
print()

cart = Purchase(buyer)
cart.add_item(hp17, 5)
cart.add_item(air_m1, 6)
print(cart)
print(cart.get_total())
