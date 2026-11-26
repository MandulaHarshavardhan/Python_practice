# def counts(s):
#     if len(s)==0:
#         return 0
#     if s[0]!='g':
#         return counts(s[1:])
#     else:
#         return 1+counts(s[1:])
# x='Programming'
# print(counts(x))   

# def fibonacci(x):
#     a,b=0,1
#     if x==0:
#         return [0]
#     elif x==1:
#         return [0,1]
#     else:
#         a=fibonacci(x-1)
#         return a+[a[-1]+a[-2]]

# a=10
# print(fibonacci(a))   

# def fibonacci(x,a=0,b=1):
#     if x==0:
#         return
#     print(a,end=" ")
#     fibonacci(x-1,b,a+b)
# a=10
# fibonacci(a)

def greater(n):#527941
    s=str(n)
    if len(s)==1:
        return s
    else:
        return max(s[0],greater(s[1:]))  
a=527941
print(greater(a))   
# 

# def removespaces(x):#hello world python 
#     if len(x)==0:
#         return " "
#     if x[0]==" ":
#         return removespaces(x[1:])
#     else:
#         return x[0]+removespaces(x[1:])
# a="hello world python"
# print(removespaces(a))  

# def countzeros(x):#1002005
#     s=str(x)
#     if len(s)==0:
#         return 0
#     if int(s[0])!=0:
#         return countzeros(s[1:])
#     else:
#         return 1+countzeros(s[1:])
# a=1002005004
# print(countzeros(a)) 
# 

# def isprime(n):#29
#     if n<2:
#         return "not a prime number !"
#     def check(divisor):
#         if divisor*divisor>n:
#             return "Prime num !"
#         if n%divisor==0:
#             return "not a prime !"
#         return check(divisor+1)
#     return check(2)  
    
    
# a=11
# print(isprime(a))   