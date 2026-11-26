# A="aabbcc"
# dici={}
# for i in A:
#     dici[i]=dici.get(i,0)+1
# if len(set(dici.values()))==1:
#     print("Equal")
# else:
#     print("Not equal")

# i=1
# pin=1231
# while i<=3:
#     lock=int(input("Enter pin : "))
#     if lock==pin:
#         print("Locker unlocked ! ")
#         break
#     print(f'You have {3-i} chances ')
#     # lock=int(input("Enter pin : "))
#     i+=1
# else:
#     print("Locker is Blocked !")

# def longest(s):
#     s=s.split()
#     idx=""
#     for i in range(len(s)):
#         if len(s[i])>len(idx):
#             idx=s[i]
#     return idx
# str="Python is an amazing programming language"
# print(longest(str))

# s=list("PyThOnProGram")
# l=0
# for r in range(len(s)):
#     if s[r].isupper():
#         s[l],s[r]=s[r],s[l]
#         l+=1
# print("".join(s))

# def exactlytwo(s):
#     dici={}
#     ans=[]
#     for i in s:
#         dici[i]=dici.get(i,0)+1
#     for k in dici:
#         if dici[k]==2:
#             ans.append(k)
#     return " ".join(ans)
# str="programming"
# print(exactlytwo(str))

# def nrc(s):
#     dici={}
#     for i in s:
#         dici[i]=dici.get(i,0)+1
#     for i in dici:
#         if dici[i]==1:
#             return i
# str="aabbccddefg"
# print(nrc(str))

li=[]
a,b=0,1
for i in range(10):
    li.append(a)
    a,b=b,a+b
for i in range(len(li)):
    if i%2!=0:
        print(li[i],end=" ")