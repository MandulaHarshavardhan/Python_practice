# s="aa33bb22"
# al=''
# di=''
# Total=''
# for i in range(len(s)):
#     if  s[i].isalpha():
#         al+=s[i]
#     elif s[i].isdigit():
#         di+=s[i]
#         if i==len(s)-1 or s[i+1].isalpha():
#             Total=Total+al*int(di)
#             al=''
#             di=''
# print(Total)


# s="aaabbccdaa"
# a=set()
# new_str=""
# for i in s:
#     if i not in a:
#         a.add(i)
#         new_str+=i
# print(new_str)

# s="Python is easy".split()#['Python','is','easy']
# for i in range(len(s)):
#     s[i]=s[i][::-1]
# print(" ".join(s))



# def removespecialchr(s):
#     new_str=""
#     for i in s:
#         if i.isalnum():
#             new_str+=i
#     # for i in s:
#     #     if not i.isalnum():
#     #        s=s.replace(i,"")
#     # return s
#     return new_str
# a="a@1#b"
# print(removespecialchr(a))


# def reversealternate(s):
#     s=s.split()
#     for i in range(len(s)):
#         if i%2!=0:
#             s[i]=s[i][::-1]
#     return " ".join(s)
# a="one two three four"
# print(reversealternate(a))


# nums = [0,0,1,1,1,2,2,3,3,4]
# new_list=[]
# a=set()
# for i in nums:
#     if i not in a:
#         a.add(i)
#         new_list.append(i)
# while len(new_list)<len(nums):
#     new_list.append('_')
# print(len(a),new_list)

# nums = [1,2,3,4]
# total=0
# for i in range(len(nums)):
#     total+=nums[i]
#     nums[i]=total
# print(nums)


def check(s1,s2):
    l=0
    r=0
    while r<len(s2):
        if r-l+1==len(s1):
            if sorted(s2[l:r+1])==sorted(s1):
                return True
            l+=1
        r+=1
    return False
s1 = "abc"
s2 = "lecabee" #lec eca cab abe bee
print(check(s1,s2))

# s1 = "abx"
# s2 = "lecabee"
# dici={}
# for i in range(len(s1), len(s2) + 1):
#     dici["".join(sorted(s2[i-len(s1):i]))]=dici.get(s2[i-len(s1):i],0)+1
# if "".join(sorted(s1)) in dici:
#     print("True")
# else:
#     print("False")




