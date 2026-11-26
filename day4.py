# sentence="python is easy python is power".split()
# dici={}
# for i in sentence:
#     if i not in dici:
#         dici[i]=1
#     else:
#         dici[i]+=1
# print(dici)       

# words=["apple","ant","ball","bat","cat","car"]
# dici={}
# for i in words:
#     if i[0] not in dici:
#         dici[i[0]]=[i]
#     else:
#         dici[i[0]].append(i)
# print(dici)    
# 

# students={
#     "A":80,
#     "B":95,
#     "c":88,
#     "D":91,
#     "E":75
# }        
# first=0
# second=0
# first_key=''
# second_key=''
# for k,v in students.items():
#     if v>first:
#         second=first
#         first=v
#         second_key=first_key
#         first_key=k
#     elif v>second and v<first:
#         second=v
#         second_key=k
# print(second_key,end=" ") 
# print(second)     

# d1={"A":10,
#     "B":20,
#     "C":30
#     }     
# d2={
#     "B":15,
#     "C":25,
#     "D":40
#     }
# merged_dici={}
# for i in d1:
#     merged_dici[i]=d1[i]
# for i in d2:
#     if i not in merged_dici:
#         merged_dici[i]=d2[i]
#     else:
#         merged_dici[i]+=d2[i]
# print(merged_dici) 

# students={
#     "Ram":95,
#     "Rahul":82,
#     "Kiran":74,
#     "Anjali":65,
#     "Vijay":45
# }       
# for k,v in students.items():
#     if v>90 and v<100:
#         students[k]='A'
#     elif v>80:
#         students[k]='B'
#     elif v>70:
#         students[k]='C' 
#     elif v>60:
#             students[k]='D'
#     else:
#         students[k]='F'
# print(students)    

# data={
#     "A":10,
#     "B":20,
#     "C":10,
#     "D":20
# }       
# new_dici={}
# for k,v in data.items():
#     if v not in new_dici:
#         new_dici[v]=[k]
#     else:
#         new_dici[v].append(k)
# print(new_dici) 

# A={1,2}
# B={1,2,3,4}
# yes=True
# for i in A:
#     if i not in B:
#         yes=False
# print(yes)    

# sentence="python is easy python is powerful".split()
# a=len(set(sentence))
# print(a)

# alphabets="abcdefxyz"
# a=[]
# for i in range(97,123):
#     if chr(i) not in alphabets:
#         a.append(chr(i))
# print(*a)        


