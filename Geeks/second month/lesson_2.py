class Person:
    def __init__(self, name, age,password):
        self.name =  name       #Публичный
        self._age = age         # Защищенный 
        self.__password = password  #Приватный


    def get_password(self):
        # Метод для получения значения приватного атрибута(Геттер)
        return self.__password
    
    def set_password(self,new_password):
        self.__password = new_password

person = Person("Geeks",4, "geeks2025")


# Публичный cпособ
# print(person.name)
# person.name = "Geektech"
# print(person.name)

# Защищенный cпособ
# print(person._age)
# person._age = 5
# print(person._age)

# Приватный cпособ
# print(person.__password)
# person.__password = "nurbolot"  
# person.__password == "nurbolot"
# print(person.__password)

# print(person.get_password())
# person.set_password("nurbolot2025")
# print(person.get_password())


class Animal:
    def speak1(self):
        return "Какой то звук"
    
class Nurbolotov1(Animal):
    def speak2(self):
        return "Гаф гаф !!!"
    
class Nurbolotov2(Animal):
    def speak3(self):
        return "Мяу мяу !!!"
    
def make_speak(geeks):
    print(geeks.hello())

print(Nurbolotov1.speak())
make_speak(Nurbolotov2())