# class BankA:
#     def __init__(self,acc_bal):
#         self.acc_bal=acc_bal
#     def deposit(self,money):
#         self.acc_bal+=money
#         print(f'{money} deposited successfully !')
#     def checkbal(self):
#         print(f'Account bal : {self.acc_bal}')
# obj1=BankA(10000)
# obj1.deposit(5000)
# obj1.checkbal()

# class Product:
#     def __init__(self,price,quantity):
#         self.price=price
#         self.quantity=quantity
#     def totalcost(self):
#         print(f'Total cost : {self.price*self.quantity}')
# p1=Product(250,4)
# p1.totalcost()

# class Temperature:
#     def __init__(self,celsius):
#         self.celsius=celsius
#     def convert(self):
#         Fahrenheit=(self.celsius*9/5)+32
#         print(f"{Fahrenheit}'F")
# t1=Temperature(25)
# t1.convert()

# class Student:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def details(self):
#         print(f'Name : {self.__name}')
#         print(f'Age : {self.__age}')
    
# s1=Student("John",21)
# s1.__name="Harsha"
# s1.details()

# class Employee:
#     def __init__(self,name,salary):
#         self.__name=name
#         self.__salary=salary
#     def getdetails(self):
#         print(f'Employee name : {self.__name}')
#         print(f'Salary : {self.__salary}')
# e1=Employee("Harsha",200000)
# e1.getdetails()

# chars=['eat','tea','tan','ate','nat','bat']
# d={}
# for i in chars:
#     s="".join(sorted(i))
#     if s not in d:
#         d[s]=[i]
#     else:
#         d[s].append(i)
# print(list(d.values()))

s="AAABABB"
k=1
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
# print(max(d.values())+k)
print(len(d))