# a=56
# while True:
#     b=int(str(a)[::-1])
#     c=a+b
#     if c == int(str(c)[::-1]):
#         print(f'palindrome Found {c}')
#         break
#     a=c

# A="aabbc"
# dici={}
# for ch in A:
#     dici[ch]=dici.get(ch,0)+1
# if len(set(dici.values()))==1:
#     print("Equal")
# else:
#     print("Not equal")    

# li=[2,3,5,7,11,13,17]
# a=[]
# for i in range(len(li)):
#     if i%2==0:
#         a.append(li[i])
# print(a)   
#     

A=[10, 20, 30, 40, 50, 60, 70]#2,5,8
B=[]
for i in range(len(A)):
    if i%3!=2:
        B.append(A[i])
print(B)    



# i=1
# setlock='1234'
# while i<=3:
#     print(f'{i}st number of attempts')
#     password=input("enter pin : ")
#     if password==setlock:
#         print("unlocked !")
#         break
#     i+=1
# else:
#     print("Locker is Blocked")  

   





