# 1 
# class Hayvon:
#     def __init__(self, nomi):
#         self.nomi = nomi
#
#     def ovoz(self):
#         print("Hayvon ovoz chiqaryapti")
#
# class It(Hayvon):
#     pass
#
# it1 = It("Rex")
# it1.ovoz()
# print(it1.nomi)




# 2
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#
#     def speak(self):
#         return "..."
#
#
# class Cat(Animal):
#     def __init__(self, name, color):
#         super().__init__(name)
#         self.color = color
#
#
#     def  speak(self):
#         super().speak()
#         print("miyov")
#
#
#
# cat = Cat('Mushuk', 'qora')
# print(cat.name)
# print(cat.color)
#
# cat.speak()




# # 3
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def introduce(self):
#         return f"Mening ismim: {self.name}"
#
#
# class Student(Person):
#     def __init__(self, name,  faculty):
#         super().__init__(name)
#         self.faculty = faculty
#
#
#     def introduce(self):
#         super().introduce()
    
    





# # 4 - misol
# class Employee:
#     def __init__(self, name):
#         self.name = name
#
#
# class Developer(Employee):
#     def __init__(self, name, stack):
#         super().__init__(name)
#         self.stack = stack
#
# dev = Developer("Alim", ["Python", "FastAPI"])
# print(dev.name, dev.stack)





# # 5 - masala
# class Shop:
#     def __init__(self, name, address):
#         self.name = name
#         self.address = address
#
#
#     def open(self):
#        print("Do`kon ochildi.")
#
#
# class OnlineShop(Shop):
#     def __init__(self, name, address, website):
#         super().__init__(name, address)
#         self.website = website
#
#     def open(self):
#         super().open()
#         print(f"Sayt manzili: {self.address}")
#
#
# shop = OnlineShop("Dokon", 'Xorazm viloyati', '....')
# print(shop.name)
# print(shop.address)
#
# shop.open()



