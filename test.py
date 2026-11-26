# class Parent:
#     def __init__(self,n):
#         self.n=n
# class Child(Parent):
#     def __init__(self,n):
#         super().__init__(n)
#     def reverse(self):
#         a=str(self.n)
#         return int(a[::-1])
# obj=Child(12345)
# print(obj.reverse())


# from abc import ABC,abstractmethod
# class Payment(ABC):
#     def __init__(self,amount):
#         self.amount=amount
#     @abstractmethod
#     def pay(self):
#         pass
# class UPI(Payment):
#     def pay(self):
#         print(f'Payment of {self.amount} processed through UPI')
# class Card(Payment):
#     def pay(self):
#         print(f'Payment of {self.amount} processed through Card')

# obj=Card(5000)
# obj.pay()


# class Calculator:

#     @staticmethod
#     def add(a, b):
#         return a + b

#     @staticmethod
#     def subtract(a, b):
#         return a - b

#     @staticmethod
#     def multiply(a, b):
#         return a * b

#     @staticmethod
#     def division(a,b):
#         return a / b
# obj=Calculator()
# print(obj.add(20,5))

# class Student:
#     def __init__(self,name,roll_no,marks):
#         self.name=name
#         self.roll_no=roll_no
#         self.marks=marks
#     def display(self):
#         print(f' Student : {self.name} , Roll No : {self.roll_no} , Marks : {self.marks}')
# s1=Student("Nani",101,85)
# s1.display()


# class Demo:
#     x=100
#     def __init__(self):
#         self.x=50
# obj=Demo()
# print(Demo.x)
# print(obj.x)







# Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

# Output: [null,null,null,null,0,null,2,1]


# class MinStack:

#     def __init__(self):
#         self.stack=[]

#     def push(self, val: int) -> None:
#         self.stack.append(val)
#     def pop(self) -> None:
#         self.stack.pop()
#     def top(self) -> int:
#         return self.stack[-1]
#     def getMin(self) -> int:
#         return min(self.stack)

tokens = ["1","2","+","3","*","4","-"]#3 3
stack=[]
for i in tokens:
    if i.isdigit():
        stack.append(int(i))
    elif i=="+":
        b=stack.pop()
        a=stack.pop()
        stack.append(a+b)
    elif i=="*":
            b=stack.pop()
            a=stack.pop()
            stack.append(a*b)
    elif i=="-":
            b=stack.pop()
            a=stack.pop()
            stack.append(a-b)
    
print(stack[-1])

