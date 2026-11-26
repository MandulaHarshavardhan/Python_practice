# def count(n):
#     if n==0:
#         return 0
#     a=n%10
#     if a>=0:
#         return 1+count(n=n//10)
#     else:
#         return count(n=n//10)
# print(count(58391))

# def palindrome(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return palindrome(s[1:-1])

# print(palindrome("madam"))

# List=[1, 2, 3, 2, 4, 2]
# element=2
# def count(sequence,n):
#     if len(sequence)==0:
#         return 0
#     for i in sequence:
#         if i==element:
#             return 1+count(sequence[1:],n)
#         else:
#             return count(sequence[1:],n)
# print(count(List,element))


# data=[
#     {'name': 'A', 'dept': 'IT', 'salary': 50000},
#     {'name': 'B', 'dept': 'IT', 'salary': 70000},
#     {'name': 'C', 'dept': 'HR', 'salary': 60000},
#     {'name': 'D', 'dept': 'HR', 'salary': 75000}
#     ]
# '''{
#     'IT': ('B', 70000),
#     'HR': ('C', 60000)
# }'''
# first=0
# second=0
# dici={}
# for i in data:
#     if i['salary']>first:
#         second=first
#         first=i['salary']
#         dici[i['dept']]=(i['name'],first)
#     elif i['salary']>second:
#         second=i['salary']
#         dici[i['dept']]=(i['name'],second)
# print (dict(sorted(dici.items(),key=lambda x:x[1],reverse=True)))


# from collections import defaultdict
# li=[1,1,2,2,2,3,4,4]
# res=defaultdict(list)
# for i in li:
#     if i in res:
#         res[i]+=1
#     else:
#         res[i]=1
# print(dict(res))

# target = 10
# position = [1,4]
# speed = [3,2]
target=12
position=[10,8,0,5,3]
speed=[2,4,1,1,3]
dici={}
for i in range(len(position)):
    time=(target-position[i])//speed[i]
    dici[time]=dici.get(time,0)+1
print(len(dici))


        