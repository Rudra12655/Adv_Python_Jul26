from Models.baseproduct import BaseProduct
from Models.descriptors import PositiveNumber
from Models.descriptors import NonEmptyString


class Product(BaseProduct):

    name = NonEmptyString()
    price = PositiveNumber()
    quantity = PositiveNumber()

    def __init__(self, name, price, quantity):

        self.name = name
        self.price = price
        self.quantity = quantity

    def display_details(self):

        print(f"""
Name      : {self.name}
Price     : {self.price}
Quantity  : {self.quantity}
""")