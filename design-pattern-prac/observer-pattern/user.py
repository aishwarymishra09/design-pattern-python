from abc import ABCMeta, abstractmethod

class IUser(metaclass=ABCMeta):
    """ the abstract class for the user  """

    @staticmethod
    @abstractmethod
    def notify(args):
        """ this method used to notify the users """

class User(IUser):

    def __init__(self, observable):
        self.obs = observable
        observable.follow(self)

    def notify(self, *args):
        print(f"{id(self)} you have status update from {id(self.obs)} is  {args}")

