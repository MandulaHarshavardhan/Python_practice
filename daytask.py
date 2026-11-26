# chars=""
# for i in range(1,101):
#     chars+=str(i)
# print(chars.count('2'))   
# 

# A='a123b4'
# cnt=0
# for i in A:
#     if i.isdigit():
#         cnt+=int(i)
# print(cnt)    


# A='a12b$#AC'
# dici={"lower":0,"upper":0,"digits":0,"specialchar":0}
# for i in A:
#     if i.isalpha():
#         if i.islower():
#             dici['lower']=dici['lower']+1
#         if i.isupper():
#             dici['upper']+=1
#     elif i.isdigit():
#         dici['digits']+=1
#     else:
#         print(i)
#         dici['specialchar']+=1
# print(dici)                            

# height = [1,8,6,2,5,4,8,3,7]
# leftwall=0
# rightwall=len(height)-1
# max_water=-1
# while leftwall<rightwall:
#     width=rightwall-leftwall
#     currheight=min(height[leftwall],height[rightwall])
#     area=width*currheight
#     max_water=max(max_water,area)
#     if height[leftwall]<height[rightwall]:
#         leftwall+=1
#     else:
#         rightwall-=1
# print(max_water)    


nums = [-1,0,1,2,-1,-4]
nums.sort()
triplets=[]
for i in range(len(nums)-2):#0,1,2,3
    if i>0 and nums[i]==nums[i-1]:
        continue
    left=i+1
    right=len(nums)-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total==0:
            triplets.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1
            while left<right and nums[left]==nums[left-1]:
                left+=1
            while left<right and nums[right]==nums[right+1]:
                right-=1
        elif total<0:
            left+=1
        else:
            right-=1
print(triplets)                                                
