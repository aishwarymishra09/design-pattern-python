from creator import Bookroom

ROOM = Bookroom().get_room("D")

# add food
ROOM.get_food()

# add speaker
ROOM.get_speaker()

# change the sheet
ROOM.sheet_change()

# get bill
print("The total bill for the Deluxe room is:  " + str(ROOM.get_bill()))
