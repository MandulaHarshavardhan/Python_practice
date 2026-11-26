# nums = [10, 15, 22, 31, 40]
# s=list(map(lambda x:x%2==0,nums))
# print(s)

# from functools import reduce
# nums = [1, 2, 3, 4, 5, 6]
# s=reduce(lambda x,y:x+y,filter(lambda x:x%2==0,nums))
# print(s)

# s = "a@b#c$d%e"
# a="".join(filter(lambda x:x.isalnum(),s))
# print(a)

# def display(n):
#     if n==0:
#         return 
#     print(n,end=" ")
#     display(n-1)
# display(5)

# def display(n):#5
#     if n==0:
#         return
#     display(n-1)
#     print(n,end=" ")
# display(5)



# s="OVZODYXAZY"
# t="XYZ"
# l=0
# r=1
# while l<len(s):
#     dici={}
#     if s[l] in t:
#         dici[s[l]]=dici.get(s[l],0)+1
#     elif s[l] not in t:
#         l+=1
#     elif s[r] in t:
#         dici[s[r]]=dici.get(s[l],0)+1
#     elif s[r] not in t:
#         r+=1
#     elif dici[s[l]]>1:
#         dici[s[l]]-=1
#         l+=1
#     elif dici[s[r]]>1:
#         dici[s[r]]-=1
#         r+=1


# s="harshavardhan"
# dici={}
# for i in s:
#     dici[i]=dici.get(i,0)+1
# a={i for i in dici.values()}
# b=sorted(list(a),reverse=True)
# second=b[1]
# for k,v in dici.items():
#     if v==second:
#         print(k)


# nums = [1,2,1,0,4,2,6]
# k = 3
# a=[]
# l=0
# r=k-1
# while r < (len(nums)):
#     if r-l+1==k:
#         a.append(max(nums[l:r+1]))
#     r+=1
#     l+=1
# print(a)



# s="abcdabasdp"
# dici={}
# for i in s:
#     dici[i]=dici.get(i,0)+1
# for k,v in dici.items():
#     if v==1:
#         print(k)
#         break

# s="abcdxeabasdp"
# seen=set()
# l=0
# max_len=0
# longest=""
# for r in range(len(s)):
#     while s[r] in seen:
#         seen.remove(s[l])
#         l+=1
#     seen.add(s[r])
#     if r-l+1 > max_len:
#         max_len=r-l+1
#         longest=s[l:r+1]
# print(max_len,longest)

def fib(n,a=0,b=1):
    if n==0:
        return 
    print(a,end=" ")
    fib(n-1,b,a+b)
fib(10)
        




        

