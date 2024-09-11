#Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
#
from abc import ABCMeta, abstractmethod
from string import printable
from typing import Self


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.square = self.length * self.width

    def __add__(self, other: Self):
        return self.square + other.square

    def __sub__(self, other: Self):
        return self.square - other.square

    def __eq__(self, other: Self):
        return (self.square == other.square)

    def __ne__(self, other: Self):
        return (self.square != other.square)

    def __lt__(self, other: Self):
        return (self.square > other.square)

    def __gt__(self, other: Self):
        return (self.square < other.square)

    def __len__(self):
        return self.width * 2 + self.length * 2


# rect = Rectangle(10, 5)
# rect1 = Rectangle(5, 2.5)
#
# print(Rectangle.__add__(rect, rect1))
# print(Rectangle.__gt__(rect, rect1))

#   ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
#
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Prince(Human):
    def __init__(self, name, age, boot):
        super().__init__(name, age)
        self.boot = boot
    def find(self, cinderella_list):
        for i in cinderella_list:
            if i.leg == self.boot:
                return i

class Cinderella(Human):

    count = 0
    def __init__(self, name, age, leg):
        Cinderella.count +=1
        super().__init__(name, age)
        self.leg = leg
    @classmethod
    def getCount(cls):
        return cls.count
    def __str__(self):
        return str(self.__dict__)


prince = Prince('Tarko', 25, 32)

cind_list = [
    Cinderella('Olya', 15, 30),
    Cinderella('Olya1', 25, 31),
    Cinderella('Olya2', 35, 32),
    Cinderella('Olya3', 45, 33),
    Cinderella('Olya4', 65, 34),
    Cinderella('Olya5', 75, 35),
    Cinderella('Olya6', 12, 36),
    Cinderella('Olya7', 32, 37),
    Cinderella('Olya7', 32, 37),
]
# print(Cinderella.getCount())
# print(Prince.find(prince, cind_list))
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
from abc import ABC, abstractmethod
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):

        print(self.name)

class Magazine(Printable):
    def __init__(self, name):
        self.name = name
    def print(self):
        print(self.name)


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name,
# та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і
# робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу
#
class Main:
    printable_list:list[Printable] = []
    @classmethod
    def add(cls, item:Book|Magazine):
        if isinstance(item,(Book, Magazine)):
            cls.printable_list.append(item)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()
# Приклад:
#
Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
