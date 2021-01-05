class Student(object):
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def __str__(self):
        return f'{self.name}, {self.age}, {self.phone}'
