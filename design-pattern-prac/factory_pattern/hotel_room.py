from abc import ABCMeta, abstractmethod


class IHotelroom(metaclass=ABCMeta):
    """ The abstraction class for the rooms """

    @staticmethod
    @abstractmethod
    def get_speaker():
        """ add speaker facility to the room """

    @staticmethod
    @abstractmethod
    def get_food():
        """ add food to the room """

    @staticmethod
    @abstractmethod
    def sheet_change():
        """ help to change the room """

    @staticmethod
    @abstractmethod
    def get_bill():
        """ get bill of the room """

