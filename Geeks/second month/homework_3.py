'''
1️⃣ Магические методы (__str__, __len__)
Задача:
Создай класс Book, у которого есть:

атрибуты title (название книги) и pages (количество страниц);
метод __str__(), который возвращает строку вида "Книга: <название>, страниц: <количество>";
метод __len__(), который возвращает количество страниц.

📌 Твоя задача – реализовать этот класс!
'''
# class Book:
#     def __init__(self, title, pages):
#         self.title = title
#         self.pages = pages

#     def __str__(self):
#         return f'Книга: {self.title}, страниц: {self.pages}'

#     def __len__(self):
#         return self.pages

# book = Book('Искусство пофигизма', 216)
# print(book)
# print(len(book))
 

'''
2️⃣ Статический метод (@staticmethod)
Задача:
Создай класс MathUtils, у которого есть:

статический метод is_even(n), который возвращает True, если число четное, и False, если нечетное;
статический метод square(n), который возвращает квадрат числа.

📌 Твоя задача – реализовать этот класс!
'''
# class MathUtils:
#     @staticmethod
#     def is_even(n):
#         return n % 2 == 0

#     @staticmethod
#     def square(n):
#         return n * n

# print(MathUtils.is_even(4)) 
# print(MathUtils.square(5))   


            

'''
Задача на ромбовидное (множественное) наследование
Создай 4 класса:

Device – базовый класс с методом info(), который выводит "Это устройство".
Smartphone – наследуется от Device, переопределяет info(), выводя "Это смартфон".
Tablet – наследуется от Device, переопределяет info(), выводя "Это планшет".
Hybrid – наследуется одновременно от Smartphone и Tablet, но не переопределяет метод info().

Твоя задача:

Реализовать все классы.
Создать объект Hybrid и вызвать info().
Вывести порядок вызова методов (MRO) с помощью print(Hybrid.mro()).
'''
class Device:
    def info(self):
        print('Это устройство')


class Smartphone(Device):
    def info(self):
        print('Это смартфон')


class Tablet(Device):
    def info(self):
        print('Это планшет')


class Hybrid(Smartphone, Tablet):
    pass

hybrid = Hybrid()
hybrid.info()
print(Hybrid.mro())
