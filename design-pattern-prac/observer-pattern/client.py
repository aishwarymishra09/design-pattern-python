from follower import Follower
from user import User


# client calling

F = Follower()
U1 = User(F)
U2 = User(F)

F.notify("today i am learning the observer pattern")