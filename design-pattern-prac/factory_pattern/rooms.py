from hotel_room import IHotelroom

class Deluxe(IHotelroom):
    """ the deluxe room of the hotel """

    def __init__(self):
        self.bill = 500

    def get_speaker(self):
        self.bill += 100

    def get_food(self):
        self.bill += 50

    def sheet_change(self):
        self.bill += 10

    def get_bill(self):
        return self.bill


class Standard(IHotelroom):
    """ the deluxe room of the hotel """

    def __init__(self):
        self.bill = 200

    def get_speaker(self):
        self.bill += 100

    def get_food(self):
        self.bill += 50

    def sheet_change(self):
        self.bill += 10

    def get_bill(self):
        return self.bill


class Business(IHotelroom):
    """ the deluxe room of the hotel """

    def __init__(self):
        self.bill = 800

    def get_speaker(self):
        self.bill += 200

    def get_food(self):
        self.bill += 100

    def sheet_change(self):
        self.bill += 10

    def get_bill(self):
        return self.bill