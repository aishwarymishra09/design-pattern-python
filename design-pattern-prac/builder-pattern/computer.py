from interface import IComputer
from product import Product


class Desktop(IComputer):
    """ the desktop class """

    def __init__(self):
        self.product = Product()


    def processor(self, pr):
        self.product.features.append(pr)
        return self

    def generation(self, pr):
        self.product.features.append(pr)
        return self

    def ram(self, pr):
        self.product.features.append(pr)
        return self

    def memory(self, pr):
        self.product.features.append(pr)
        return self

    def type(self):
        self.product.features.append("Desktop")
        return self

    def get_result(self):
        return self.product.features


class Laptop(IComputer):
    """ the desktop class """

    def __init__(self):
        self.product = Product()

    def processor(self, pr):
        self.product.features.append(pr)
        return self

    def generation(self, pr):
        self.product.features.append(pr)
        return self

    def ram(self, pr):
        self.product.features.append(pr)
        return self

    def memory(self, pr):
        self.product.features.append(pr)
        return self

    def type(self):
        self.product.features.append("Laptop")
        return self

    def get_result(self):
        return self.product.features
