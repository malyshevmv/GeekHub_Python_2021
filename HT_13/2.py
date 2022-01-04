"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів,
які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_age(self):
        print(self.age)

    def print_name(self):
        print(self.name)

    def show_all_information(self):
        for k, v in self.__dict__.items():
            print(f'{k}: {v}')


obj1 = Person('name_obj1', 11)
obj1.show_all_information()
obj1.profession = 'profession_obj1'
print()
obj1.show_all_information()
print('------------')
obj2 = Person('name_obj1', 121)
obj2.show_all_information()
obj2.profession = 'profession_obj2'
print()
obj2.show_all_information()
