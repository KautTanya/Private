"""Metaclass private"""


class PrivateMeta(type):
    """Metaclass"""
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        # print("Yes")
        for key, value in attrs.items():
            if key.startswith("__"):
                new_key = "__private_" + key[2:]
                new_attrs[new_key] = value
            else:
                new_attrs[key] = value
        # print(new_attrs)
        return super().__new__(cls, name, bases, new_attrs)


class NewClass(metaclass=PrivateMeta):
    """New class"""
    def __init__(self):
        self.__private_attribute = 20

    def example(self):
        """example"""
        pass


# Перевірка
obj = NewClass()
print(dir(NewClass))
