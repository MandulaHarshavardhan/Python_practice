# def bus_stops(stops):
#     for i in stops:
#         yield i
# stops=input("enter stops : " ).split()
# for i in bus_stops(stops):
#     print(i)   
# 

# def fibonacci(n):
#     a=0
#     b=1
#     for i in range(n):
#         yield i
#         a,b=b,a+b
# for i in fibonacci(10):
#     print(i)        

# def numbers():
#     yield 1
#     yield 2
#     yield 3
# x=numbers()
# print(next(x)) 
# print(next(x)) 


# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# x=5
# print(factorial(x))   
# 

# def reverse(s):
#     if len(s)<=1:
#         return s
#     else:
#         return reverse(s[1:])+s[0]
# x="Harsha"
# print(reverse(x)) 
# 

# def palindrome(s,l,r):
#     if l>=r:
#         return True
#     if s[l]!=s[r]:
#         return False
#     return palindrome(s,l+1,r-1)
# x="madam"
# print(palindrome(x,0,len(x)-1)) 
# 

# from functools import reduce
# a=[1,2,3,4,5]
# res=reduce(lambda x,y:x+y,a)
# print(res)     
# 

# def total(l):
#     if len(l)==0:
#         return 0
#     else:
#         return l[-1] + total(l[:-1])
# a=[1,2,3,4,5]
# print(total(a))  

#Hello Ravi, you are 21 years old. 
def display(name,age):
    print(f'Hello {name}, you are {age} years old  ')
display("Harsha",22)
