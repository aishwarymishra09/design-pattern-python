# pylint: disable=too-few-public-methods

from abc import ABCMeta, abstractmethod

class ISubject(metaclass=ABCMeta):
    "abstract method for the observable"

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        "A method to subscribe the observer"


    @staticmethod
    @abstractmethod
    def unsubscribe(observer):
        "A method to unsubscribe the observer"

    @staticmethod
    @abstractmethod
    def notify(observer):
        "A method to notify all the observer"

class Subject(ISubject):

    def __init__(self):
       self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)


    def unsubscribe(self, observer):
        self._observers.remove(observer)


    def notify(self, *args):
        for observer in self._observers:
            observer.notify(*args)


class IObserver(metaclass=ABCMeta):
    "An abstract class for the observer"

    @staticmethod
    @abstractmethod
    def notify(observable, *args):
        "this method is for the notify"

class Observer(IObserver):

    def __init__(self, observable):
        self. obs = observable
        self.obs.subscribe(self)

    def unsubscribe(self):
        self.obs.unsubscribe(self)

    def notify(self, *args):
        print(f"this observer {id(self)} to notify {args}")




s = Subject()
o1 = Observer(s)
o2 = Observer(s)

s.notify("aaa")

