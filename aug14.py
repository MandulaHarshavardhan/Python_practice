# s="banana"
# def frequency(s):
#     dici={}
#     for i in s:
#         if i not in dici:
#             dici[i]=1
#         else:
#             dici[i]=dici.get(i,0)+1
#     for k,v in dici.items():
#         yield k,v 
# for k,v in frequency(s):
#     print(k,v)
# #print(next(frequency(s)))   

# def isleapyear(y):
#     if (y%4==0 and y%100!=0) or y%400==0:
#         return True
#     else:
#         return False
# def leapyears(a,b):#2000 2020
#     for i in range(a,b+1):
#         if isleapyear(i):
#             yield i
# for i in leapyears(2000,2021):
#     print(i,end=" ")

# class Temperature:
#     def __init__(self,t):
#         self.__temp=t
#     def isvalid(self):
#         if self.__temp>=-273:
#             return "Valid Temperature"
#         else:
#             return "Invalid Temperature"
# n=int(input("Enter Temoerature : "))
# a=Temperature(n)
# print(a.isvalid())

# class Payment:
#     def __init__(self,b,p):
#         self.__balance=b
#         self.topay=p
#     def todo(self):
#         if self.topay<=self.__balance:
#             print("Payment Successful !")
#             self.__balance-=self.topay
#             return self.__balance
#         else:
#             return "Insufficient balance :("
# a=Payment(3000,3200)
# print(a.todo())

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def check(self):
#         if self.marks>=35:
#             return f"{self.name} is Passed "
#         else:
#             return f"{self.name} is Failed"
# obj=Student("Abhi",15)
# print(obj.check())