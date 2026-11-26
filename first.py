# def secondsmallest(x):
#     b=list(set(a))
#     for i in range(len(b)-1):
#         if b[i]>b[i+1]:
#             b[i],b[i+1]=b[i+1],b[i]
#     return b[1]


# a=[12, 8, 15, 8, 20, 5, 5]
# res=secondsmallest(a)
# print(res)


# def rotaterightby(a,x):
#     a=a[k:]+a[:k]
#     return a
# a=(10, 20, 30, 40, 50)
# k=2
# res=rotaterightby(a,k)
# print(res)

# def exactlytwo(A,B,C):
#     D=[]
    
#     for i in A|B|C:
#         cnt=0
#         if i in A:
#             cnt+=1
#         if i in B:
#             cnt+=1
#         if i in C:
#             cnt+=1
#         if cnt==2:
#             D.append(i)
#     return set(D)        
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# C = {4, 5, 6, 7}
# res=exactlytwo(A,B,C)
# print(res)


# A={'A': 85, 'B': 92, 'C': 78, 'D': 88}  
# B=dict(sorted(A.items(),key=lambda x:x[1],reverse=True))
# for i,key in enumerate(B,start=1):
#     B[key]=i
# print(B)    


A=[1, 2, 3, 4, 5]
B=[3, 4, 5, 1, 2]
found=False
for i in range(len(A)):#0,1,2,3,4
    rotated=A[i:]+A[:i]
    if rotated==B:
        found=True
        break
print(found)    



