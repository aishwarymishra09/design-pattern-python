from abc import ABCMeta, abstractmethod

class IComputer(metaclass=ABCMeta):
    """ This is abstract class for the computer """

    @staticmethod
    @abstractmethod
    def processor(feature):
        """ add processor to the compupter"""

    @staticmethod
    @abstractmethod
    def generation(feature):
        """ add the generation to the computer """

    @staticmethod
    @abstractmethod
    def ram(feature):
        """ declares the ram to the computer """

    @staticmethod
    @abstractmethod
    def memory(feature):
        """ declares the memory of the computer"""

    @staticmethod
    @abstractmethod
    def type():
        """ either Laptop or DeskTop """
