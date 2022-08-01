# Task:
# 2) Создайте декоратор класса с параметром. Параметром должна быть
# строка, которая должна дописываться (слева) к результату работы метода
# __str__.

def add_to_str(text):
    '''
    appends a string (on the left) 
    to the result of the __str__ method 
    '''
    def inner_1(cls):
        def inner_2(*args, **kwargs):
            new_instance = cls(*args, **kwargs)
            return f'{text} {new_instance}'
        return inner_2
    return inner_1


@add_to_str('Student:')
class Student:

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'


st = Student('John', 'Doe')
print(st)
