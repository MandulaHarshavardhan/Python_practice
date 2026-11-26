# def fib(n,a=0,b=1):
#     if n==0:
#         return
#     print(a,end=" ")
#     fib(n-1,b,a+b)
# fib(7)

# s="hello world"
# def repspaces(s):
#     if s=="":
#         return ""
#     if s[0]==" ":
#         return "-"+ repspaces(s[1:])
#     return s[0]+repspaces(s[1:])
# print(repspaces(s))

# nums=[-5, 2, -1, 7, 0]
# s=list(filter(lambda x:x<0,nums))
# print(s)

# nums=[121, 123, 454, 678]
# def ispalindrome(n):
#     c=n
#     a=0
#     while n>0:
#         a=a*10+(n%10)
#         n//=10
#     return a==c
# s=list(filter(ispalindrome,nums))
# print(s)

# d=list(filter(lambda x:str(x)==str(x)[::-1],nums))
# print(d)

from functools import reduce
# nums=[2, 3, 4, 5]
# s=reduce(lambda x,y:x*y,nums)
# print(s)

nums=[12, 45, 7, 89, 23]
s=reduce(lambda x,y: x if x>y else y,nums)
print(s)


