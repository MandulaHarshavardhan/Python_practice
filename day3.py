# def longestword(x):
#     x=str.split()
#     idx=""
#     for i in range(len(x)):#0,1,2,3,4,5
#         if len(x[i]) > len(idx):
#             idx=x[i]
#     return idx
# str="Python is an amazing programming language"   
# print(longestword(str))

# s=list("PyThOnProGram")
# # left=""
# # right=""
# # for i in str:
# #     if i.isupper():
# #         left+=i
# #     else:
# #         right+=i
# # print(left+right)  
# l=0
# for r in range(len(s)):
#     if s[r].isupper():
#         s[l],s[r]=s[r],s[l]
#         l+=1
# print("".join(s))     
# 



# def exactlytwo(s):
#     dici={}
#     ans=[]
#     for i in s:
#         if i not in dici:
#             dici[i]=1
#         else:
#             dici[i]+=1
#     for k,i in dici.items():
#         if dici[k]==2:
#             ans.append(k)
#     return " ".join(ans)   
# s="programming"
# print(exactlytwo(s))


# def abc(s):
#     dici={}
#     for i in s:
#         dici[i]=dici.get(i,0)+1
#     for i in dici:
#         if dici[i]==1:
#             return i
# s="aabbccddefg"
# print(abc(s))

def isrotation(s1,s2):
        
    found=False
    for i in range(len(s1)):
        s1=s1[i:]+s1[:i]
        if s1==s2:
            found=True
    return found 
s1="rotation"
s2="tionrota" 
print(isrotation(s1,s2))




    




