'''
🔹 Задачи по Инкапсуляции 
1️⃣ Контроль температуры
Задача:
Создай класс Thermometer, у которого:

Приватный атрибут __temperature (температура).
Метод set_temperature(value), который меняет температуру только в диапазоне от -50 до 150.
Метод get_temperature(), который возвращает текущую температуру.

Твоя задача:
Создать объект, попробовать установить температуру выше 150 или ниже -50, проверить, 
что температура не изменилась.
'''
# class Thermometer:
#     def __init__(self):
#         self.__temperature = 0

#     def set_temperature(self, value):
#         if -50 <= value <= 150:
#             self.__temperature = value

#     def get_temperature(self):
#         return self.__temperature

# thermometer=Thermometer()
# thermometer.set_temperature(200)  
# print(thermometer.get_temperature())  
# thermometer.set_temperature(-60) 
# print(thermometer.get_temperature())  
# thermometer.set_temperature(25)
# print(thermometer.get_temperature()) 


 
'''
2️⃣ Секретный код
Задача:
Создай класс SafeBox, у которого:

Приватный атрибут __code (секретный код, задаётся при создании).
Метод unlock(code), который открывает сейф только если код совпадает.
Метод change_code(old_code, new_code), который меняет код только если введён правильный старый код.

Твоя задача:
Создать сейф, попробовать открыть его с неправильным кодом, затем изменить код и снова попробовать открыть.
'''
# class SafeBox:
#     def __init__(self, code):
#         self.__code = code

#     def unlock(self, code):
#         return code == self.__code

#     def change_code(self, old_code, new_code):
#         if old_code == self.__code:
#             self.__code = new_code
#             return True
#         return False

# safe=SafeBox('1234')
# print(safe.unlock('0000'))  
# print(safe.change_code('0000', '5678'))  
# print(safe.change_code('1234', '5678'))  
# print(safe.unlock('5678'))  



'''
🔹 Задачи по Полиморфизму
3️⃣ Разные виды транспорта
Задача:
Создай базовый класс Transport с методом move(), который выводит "Перемещение...".
Создай три подкласса:

Car, у которого move() выводит "Машина едет по дороге".
Boat, у которого move() выводит "Лодка плывёт по воде".
Plane, у которого move() выводит "Самолёт летит в небе".

Твоя задача:
Создать список с разными транспортами и вызвать move() для каждого.
'''
# class Transport:
#     def move(self):
#         print('Перемешение...')

# class Car(Transport):
#     def move(self):
#         print('Машина едет по дороге')

# class Boat(Transport):
#     def move(self):
#         print('Лодка плывет по воде')

# class Plane(Transport):
#     def move(self):
#         print('Самолет летит в небе')

# vehicles=[Car(), Boat(), Plane()]
# for vehicle in vehicles:
#     vehicle.move()



 
'''
4️⃣ Разные типы файлов
Задача:
Создай базовый класс File, у которого есть метод open(), который выводит "Файл открыт".
Создай три подкласса:

TextFile, у которого open() выводит "Открыт текстовый файл".
ImageFile, у которого open() выводит "Открыто изображение".
AudioFile, у которого open() выводит "Открыт аудиофайл".

Твоя задача:
Создать список файлов разных типов и вызвать open() для каждого.
'''
# class File:
#     def open(self):
#         print('Файл открыт')

# class TextFile(File):
#     def open(self):
#         print('Открыт текстовый файл')

# class ImageFile(File):
#     def open(self):
#         print('Открыто изображение')

# class AudioFile(File):
#     def open(self):
#         print('Открыт аудиофайл')

# files=[TextFile(), ImageFile(), AudioFile()]
# for file in files:
#     file.open()



'''
🔹 Задача на Инкапсуляцию + Полиморфизм
5️⃣ Игровые персонажи
Задача:
Создай класс Character, у которого:

Приватный атрибут __health (здоровье).
Метод take_damage(amount), который уменьшает __health, но не ниже 0.
Метод get_health(), который возвращает текущее здоровье.
Создай три подкласса:

Warrior, который при take_damage() получает на 20% меньше урона.
Mage, который получает обычный урон.
Robot, который получает на 50% меньше урона.
Твоя задача:
Создать каждого персонажа, нанести им урон и сравнить здоровье.
'''
class Character:
    def __init__(self):
        self.__health = 100

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def get_health(self):
        return self.__health

class Warrior(Character):
    def take_damage(self, amount):
        super().take_damage(amount * 0.8)

class Mage(Character):
    pass

class Robot(Character):
    def take_damage(self, amount):
        super().take_damage(amount * 0.5)

warrior=Warrior()
mage=Mage()
robot=Robot()

warrior.take_damage(50)
mage.take_damage(50)
robot.take_damage(50)

print('Warrior health:', warrior.get_health()) 
print('Mage health:', mage.get_health())  
print('Robot health:', robot.get_health())  
