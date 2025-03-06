# class Aboutme:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def print_info(self):
#         print(f"Имя: {self.name}, возраст: {self.age}")


# about = Aboutme("Морген", 38)

# about.print_info()


# class Aboutme:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Имя: {self.name}, возраст: {self.age}"


# about = Aboutme("Морген", 38)
# print(about)


# class Group:
#     def __init__(self,students):
#         self.students = students

#     def __len__(self):
#         return len(self.students)
    
# group = Group(["Али", "Бекболсун", "Айгерим"])
# print(len(group))





# class Math:
#     a = 4
#     b = 3
#     def add(self):
#         print(self.a + self.b)



class Math:
    
    @staticmethod
    def add(num1, num2):
        return num1 +num2
    


print(Math.add(5,8))