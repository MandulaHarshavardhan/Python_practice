# class Operation:
#     def calculate(self):
#         pass
# class Addition(Operation):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def calculate(self):
#         print(self.a+self.b)
# class Multiplication(Operation):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def calculate(self):
#         print(self.a*self.b)
# obj=Addition(10,5)
# obj.calculate()
# obj=Multiplication(10,5)
# obj.calculate()


# class Number:
#     def __init__(self,n):
#         self.n=n
# class Pattern(Number):
#     def __init__(self,n):
#         Number.__init__(self,n) #super().__init__(n)
#     def print_pattern(self):
#         for i in range(1,self.n+1):
#             for j in range(1,i+1):
#                 print(j,end=" ")
#             print()
# obj=Pattern(4)
# obj.print_pattern()

# class SecurePin:
#     def __init__(self):
#         self.__pin=None
#     def storepin(self,pin):
#         self.__pin=pin
#     def sum_of_pin(self):
#         res=0
#         while self.__pin>0:
#             res+=self.__pin%10#6,2,8,4
#             self.__pin//=10
#         print(res)
# obj=SecurePin()
# obj.storepin(4826)
# obj.sum_of_pin()


# class Number:
#     def __init__(self,n):#58321
#         self.n=n
# class DigitDifference(Number):
#     def __init__(self,n):
#         super().__init__(n)
#     def display(self):
#         largest=int(max(str(self.n)))
#         smallest=int(min(str(self.n)))
#         print(largest-smallest)
# obj=DigitDifference(58321)
# obj.display()

class PatternInput:
    def __init__(self,n):#4
        self.n=n
class ReversePattern:
    def __init__(self,n):
        PatternInput.__init__(self,n)
    def display(self):
        for i in range(self.n,0,-1):#4 3 2 1
            for j in range(i):
                print(i,end=" ")
            print()
obj=ReversePattern(4)
obj.display()

