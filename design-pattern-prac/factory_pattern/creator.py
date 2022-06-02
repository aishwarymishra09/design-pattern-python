from rooms import Deluxe, Standard, Business

class Bookroom:
    """ creator class to book room """

    def get_room(self, rtype:str):
        if rtype == "D":
            room = Deluxe()
        elif rtype == "S":
            room = Standard()
        else:
            room = Business()
        return room


