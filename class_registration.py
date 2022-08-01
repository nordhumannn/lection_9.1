# Task:
# 1) Создайте декоратор, который зарегистрирует декорируемый класс в
# списке классов.

class_list = []


def class_registration(cls):
    '''
    adds the decorated class to
    the list of classes (class_list)
    '''
    class_list.append(cls)


@class_registration
class Box:

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'x = {self.x}, y = {self.y}, z = {self.z}'


@class_registration
class Student:

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'Name: {self.name}'


print(class_list)
