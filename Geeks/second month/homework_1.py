'''
Задача 1: Класс "Книга"
Создай класс Book, у которого есть:
Атрибуты: title (название книги), author (автор), year (год издания).
Метод display_info(), который выводит информацию о книге.
Создай несколько объектов этого класса и вызови метод display_info().
 '''

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year

#     def display_info(self):
#         print(f'Название книги: {self.title}, Автор: {self.author}, Год издания: {self.year}')

# book1 = Book('Искусство пофигизма', 'Марк Мэнсон', 2016)
# book2 = Book('Не ной', 'Джен Синсеро', 2019)

# book1.display_info()
# book2.display_info()



'''
Задача 2: Класс "Банковский счет"
Создай класс BankAccount, который содержит:
Атрибут balance (баланс, начальное значение 0).
Методы deposit(amount), withdraw(amount), которые пополняют и снимают деньги.
Метод display_balance(), который показывает текущий баланс.
Создай объект счета, проведи несколько операций и выведи баланс.
'''
# class BankAccount:
#     def __init__(self):
#         self.balance = 0
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f'Пополнение: +{amount} сом. Текущий баланс: {self.balance} сом')
#         else:
#             print('Сумма должна быть положительной!')
    
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f'Снятие: -{amount} сом. Текущий баланс: {self.balance} сом')
#         else:
#             print('Недрстаточно средств или некорректная сумма!')
    
#     def display_balance(self):
#         print(f'Текущий баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(5000)
# account.withdraw(2000)
# account.deposit(3000)
# account.withdraw(7000)
# account.display_balance()

    
 
'''
Задача 3: Класс "Автомобиль" с атрибутами и методами
Создай класс Car, который имеет:

Атрибуты: brand (марка), model (модель), year (год выпуска).
Метод start(), который выводит Машина {brand} {model} завелась!.
Метод stop(), который выводит Машина {brand} {model} заглушена..
Создай объект и протестируй методы.
 '''
# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
    
#     def start(self):
#         print(f'Машина {self.brand} {self.model} завелась!')
    
#     def stop(self):
#         print(f'Машина {self.brand} {self.model} заглушена.')

# car = Car('KIA', 'k3', 2023 )
# car.start()
# car.stop()



'''
Задача 4: Наследование "Животные"
Создай родительский класс Animal, который имеет:
Атрибут name.
Метод speak(), который выводит "Животное издает звук".
Создай два дочерних класса:
Dog, который переопределяет speak(), выводя "Собака лает: Гав-гав!".
Cat, который переопределяет speak(), выводя "Кот мяукает: Мяу!".
Создай объекты Dog и Cat, вызови speak().
 '''
# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#         print('Животное издает звук')

# class Dog(Animal):
#     def speak(self):
#         print(f'Собака {self.name} лает: Гав-гав!')

# class Cat(Animal):
#     def speak(self):
#         print(f'Кот {self.name} мяукает: Мяу!')

# # Пример использования
# dog = Dog('Kripto')
# cat = Cat('Matroscin')
# dog.speak()
# cat.speak()

    
''' 
Задача 5: Класс "Студент" и наследование
Создай класс Student, который содержит:
Атрибуты: name (имя), age (возраст), group (группа).
Метод introduce(), который выводит Меня зовут {name}, мне {age} лет, я учусь в группе {group}.
Создай дочерний класс ExcellentStudent, который:
Наследует Student.
Добавляет атрибут gpa (средний балл).
Переопределяет introduce(), добавляя "У меня отличный средний балл: {gpa}!".
Создай объекты обоих классов, вызови introduce().
'''
# class Student:
#     def __init__(self, name, age, group):
#         self.name = name
#         self.age = age
#         self.group = group

#     def introduce(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет, я учусь в группе {self.group}.')

# class ExcellentStudent(Student):
#     def __init__(self, name, age, group, gpa):
#         super().__init__(name, age, group)
#         self.gpa = gpa

#     def introduce(self):
#         print(f'Меня зовут {self.name}, мне {self.age} лет, я учусь в группе {self.group}. У меня отличный средний балл: {self.gpa}!')

# student = Student('Бекзат', 18, 'ПМИ-2-24')
# excellent_student = ExcellentStudent('Бека', 18, 'Geeks 26-1B', 92)

# student.introduce()
# excellent_student.introduce()
