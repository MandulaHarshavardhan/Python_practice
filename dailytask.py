# x=[10, 12, 15, 17, 21, 25, 30]
# output=list(filter(lambda n:n%3==0,x))
# print(output)

# nums=[2,4,6,8]
# res=list(map(lambda x:x**2,nums))
# print(res)

# from functools import reduce
# nums=[2, 3, 4, 5]
# res=reduce(lambda x,y:x*y,nums)
# print(res)

# nums=[1, 2, 3, 4, 5, 6, 7, 8]
# # even=list(filter(lambda x:x%2==0,nums))
# # res=list(map(lambda x:x**2,even))
# res=list(map(lambda x:x**2 ,list(filter(lambda x:x%2==0,nums))))
# print(res)


# def find_largest(*args):
#     a=[i for i in args]
#     a.sort()
#     return a[-1]
# print(find_largest(15, 42, 7, 89, 31, 64))

# def students(**kwargs):#name='Ravi
#     for k,v in kwargs.items():
#         print(f'{k}:{v}')  
# students(name="Ravi", age=21, course="Python", marks=85)

# a=[("Ravi", 85), ("Anil", 72), ("Kiran", 91), ("Sita", 78)]
# res=sorted(a,key=lambda x:x[1])
# print(res)

# from functools import reduce
# a=[5, 12, 8, 15, 20, 3, 25]
# res=reduce(lambda x,y:x+y,map(lambda x:x*2,filter(lambda x:x>10,a)))
# print(res)

from functools import reduce
a=[3, 6, 9, 12, 15, 18]
res=reduce(lambda x,y:x+y,map(lambda x:x**2,filter(lambda x:x%3==0,a)))
print(res)

