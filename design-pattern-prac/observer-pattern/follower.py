from abc import ABCMeta, abstractmethod


class IFollower(metaclass=ABCMeta):
    """This is an abstract class for the follower class, a type of observable"""

    @staticmethod
    @abstractmethod
    def follow(observer):
        """this is used to add follower"""

    @staticmethod
    @abstractmethod
    def unfollow(observer):
        """remove follower from the list"""

    @staticmethod
    @abstractmethod
    def notify(observer):
        """notify all the followers"""


class Follower(IFollower):
    def __init__(self):
        self.followers = set()

    def follow(self, observer):
        """add followers to follower list"""

        self.followers.add(observer)

    def unfollow(self, observer):
        """remove this from the follower list"""

        self.followers.remove(observer)

    def notify(self, *args):
        for follower in self.followers:
            follower.notify(args)
