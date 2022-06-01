from abc import ABCMeta, abstractmethod


class IBuilder(metaclass=ABCMeta):
    """ This is the builder interface"""

    @staticmethod
    @abstractmethod
    def method_a(observer):
        """ this is one method or feature"""

    @staticmethod
    @abstractmethod
    def method_b():
        """this is another feature"""

    @staticmethod
    @abstractmethod
    def method_c():
        """this is another feature"""

    @staticmethod
    @abstractmethod
    def get_result():
        """ It returns the final product """


class Builder(IBuilder):
    """ Actual builder class"""

    def __init__(self):
        self.product = Product()

    def method_a(self, observer):
        self.product.parts.append(observer)
        return self

    def method_b(self):
        self.product.parts.append("b")
        return self

    def method_c(self):
        self.product.parts.append("c")
        return self

    def get_result(self):
        return self.product


class Product:
    """ This is a product class"""

    def __init__(self):
        self.parts = []


class Director:
    """ It is the executable class, it gives the product, implimnting the complex representation"""

    @staticmethod
    def construct():
        """ This method is used to construct the real product"""
        return Builder().method_a("lappy") \
            .method_b().get_result()


d = Director().construct()
print(d.parts)
