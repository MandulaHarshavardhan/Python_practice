from collections import defaultdict
# Math={'Rahul':90,'Kiran':80}
# Science={'Rahul':88,'Kiran':85}
# res=defaultdict(list)#{}
# for k,v in Math.items():
#     res[k].append(v)
# for k,v in Science.items():
#     res[k].append(v)
# print(dict(res))

# chrs=["eat","tea","ate","tan","nat","bat"]
# res=defaultdict(list)
# for s in chrs:
#     counts=[0]*26
#     for c in s:
#         counts[ord(c)-ord('a')]+=1
#     res[tuple(counts)].append(s)
# print(list(res.values()))

# import math
# nums=[1,2,3,4]
# product=math.prod(nums)
# for i in range(len(nums)):#0,1,2,3
#     nums[i]=product//nums[i]
# print(nums)

# nums=[1,2,3,4]
# res=[1]*len(nums)
# prefix=1
# for i in range(len(res)):
#     res[i]=prefix
#     prefix*=nums[i]
# postfix=1
# for i in range(len(res)-1,-1,-1):
#     res[i]*=postfix
#     postfix*=nums[i]
# print(res)

# class CricketPlayer:
#     def __init__(self,player_name,runs,matches):
#         self.player_name=player_name
#         self.runs=runs
#         self.matches=matches
#     def player_details(self):
#         print(f'Player Name : {self.player_name}')
#         print(f'Runs : {self.runs}')
#         print(f'Matches : {self.matches}')
# obj1=CricketPlayer('Virat Kohli',13848,302)
# obj1.player_details()

# class Student:
#     college="ABC"
# s1=Student()
# s2=Student()
# s1.college="XYZ"
# print(s1.college)
# print(s2.college)

class Student:
    count=0
    def __init__(self):
        Student.count+=1
Student()
Student()
Student()
print(Student.count)

