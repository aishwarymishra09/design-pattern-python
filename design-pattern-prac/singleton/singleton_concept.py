class Singleton:
    """" A singleton class can be initiated any number of times but only a sigle refrence created"""
    records = []

    # have a class variable and work on it
    def __new__(cls):
        return cls

    @classmethod
    def append_number(cls, num):
        cls.records.append(num)
        return cls.records


# check if to intiation refer to the same reference

s1 = Singleton()
s2 = Singleton()

print(id(s1))
print(id(s2))

# if methods are working well
print(s1.append_number(2))
print(s2.append_number(3))
