# name = "Nurbolot"  #переменная
# def display()   #функция

# class Car:
#     brand = "Tayota"  # Атрибут
#     model = "Camry"  # Атрибут

#     def display(self):  #метод
#         print(f"Название {self.brand}, Модель: {self.model}")

# car = Car()

# car.display()

# print - выводит
# return - возвращает

# class Animals:
#     cow = "Корова"

#     def speak(self):
#         print("Муу муу муу")

#     def jump(self):
#         return f"{self.cow} пригает"
    
# animals = Animals()

# # animals.speak()
# print(animals.jump())


class Person:
    name = "Nurbolot"
    age = 25
    def info(self):
        print(f"Имя: {self.name1}, возраст: {self.age1}")

person = Person()
person.info()


class Person:
    def __init__(self,name,age,pol):
        self.name = name
        self.age = age
        self.pol = pol

    def info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")
        print(f"Пол: {self.pol}")

person = Person("Бекболсун",18,"Мужской")
person2 = Person("Айжамал",18,"женский")

person.info()
print("    ")
person2.info()


class Dad:
    car = "BMW"
    home = "5 комнатный"

    def smeh(self):
        print("Ho ho ho ho")

class Mom:
    def haracter(self):
        print("Жестокость")

    def crasota(self):
        print("Красивые глаза")
        
class Son(Dad,Mom,):
    hair = "Волосы"

son = Son()
son.smeh()
son.haracter()


class Dad:
    car = "BMW"
    home = "5 комнатный"

    def smeh(self):
        print("Ho ho ho ho")


class Son(Dad,):
    hair = "Волосы"

class Doch(Dad,):
    brain = "Ум"

son = Son()
son.smeh()
son.haracter()

# Создайте Род класс Animal с методом speak, и "движение"
# Создайте дочерьний класс Cat и Dog c методом Пригать и цвет


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} издает звук")

    def dvij(self):
        print(f"{self.name} бегает ")

class Cat(Animal):
    def __init__(self,name,kuda,color):
        super().__init__(name)
        self.kuda = kuda
        self.color = color

    def jump(self):
        print(f"{self.name} прыгает {self.kuda}")

    def color_a(self):
        print(f"{self.name} - {self.color} цвета")

cat = Cat("Мышык", "на крышу", "черный")
cat.speak()
cat.jump()
cat.color_a()