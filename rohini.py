# // print

# print("hellow world")

# a = 10
# b = 0.343
# c = "rohini"
# d = True
# print(type(d))


# // input
# // data -> a = 
# a = int(input("enter a number "))

# age = int (input("enter you age: "))
# if(age > 18):
#     print ( "you can vote")
# else:
#     print("you can not vote")





#  if else
# (), {}, []  

# t = (2,3,4,5)

# d = { "name" : "rohini", "age" : 22}


# print(d["age"])

# a = [2,3,4,5,6]

# for i in a:
#     print(i)

# print(a[-1])


#  loop -> for , while
#  
# // function -> block of code
#  class -> 
#  object 
#  exception 
# 


# def print_name(a,b,c):
#     print(a)
#     print(b)
#     print(c)


# print_name("rohini","22","python")

# class car:
#     def __init__(self,name, model):
#         self.name=name
#         self.model = model

#     def display(self):
#         print( f"car name: {self.name} \ model of car: {self.model}")

# class Bank:

#     def __init__(self, Name, city):
#         self.name = Name
#         self.city = city

#     def show_detail(self):
#         return f"bank name: {self.name} City: {self.city}"

# class Customer(Bank):
#     def __init__(self, Name, city, customer_name, address):
#         super().__init__(Name, city)
#         self.customer_name= customer_name
#         self.address = address

#     def show_detail(self):
#         bank = super().show_detail()
#         return f"Bank Detail: {bank} \n Customer: Name: {self.customer_name} Address: {self.address}"

#     def __str__(self):
#         return "he ist me"

# cus1 = Customer("SBI", "Pune", "rohini", "Pune")
# print(cus1.__str__())
# print(cus1.show_detail())
# print(cus1.city)
        

# import math
# a= math.sqrt(16)
# print(a)