# # A=['flower','f','flight']
# # prefix=A[0]
# # for i in A[1:]:
# #     while not i.startswith(prefix):
# #         prefix=prefix[:-1]

# # print(prefix)        

# x=[1,[2,3],[4,5,[6,7],8],9]
# output=[]
# def flattern(y):
#     for i in y:
#         if type(i)!=list:
#             output.append(i)
#         else:
#             flattern(i)
        
# flattern(x)
# print(output)   
             
from functools import reduce
x=[1,2,3,4]
res=reduce(lambda x,y:x*y,x)
print(res)