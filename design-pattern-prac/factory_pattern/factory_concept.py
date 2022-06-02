from abc import ABCMeta, abstractmethod


class IProduct(metaclass=ABCMeta):
    """ The interface class of the Products """

    @staticmethod
    @abstractmethod
    def product_name():
        """ provides the name of the product """


class ProductA(IProduct):
    """ the product A"""

    def __init__(self):
        self.name = "product_a"

    def product_name(self):
        return self


class ProductB(IProduct):
    """ the product B"""

    def __init__(self):
        self.name = "product_b"

    def product_name(self):
        return self


class ProductC(IProduct):
    """ the product C"""

    def __init__(self):
        self.name = "product_c"

    def product_name(self):
        return self


class Creator:
    """The factory class"""

    @staticmethod
    def get_product(first_letter):
        if first_letter == "a":
            pr = ProductA()
        elif first_letter == "b":
            pr = ProductB()
        else:
            pr = ProductC()
        return pr


product = Creator.get_product("c")
print(product.name)
