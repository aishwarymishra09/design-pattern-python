from creator import Bookroom

ROOM = Bookroom().get_room("D")

# add food
ROOM.get_food()

# add speaker
ROOM.get_speaker()

# change the sheet
ROOM.sheet_change()

# get bill
print(ROOM.get_bill())
