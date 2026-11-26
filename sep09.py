# s = "dfa123423afd"
# nums_count=set()
# first=float("inf")#1
# second=float("inf")
# for i in s:
#     if i.isdigit():
#         nums_count.add(int(i))
#         if int(i)<first:
#             first=int(i)
#         elif int(i)<second and int(i)>first:
#             second=int(i)
# if len(nums_count)<2:
#     print("-1")
# else:
#     print(second)

# nums = [10,20,30,40,5,10,50,40,50,55,50]
# max_sum=0
# total=0
# for i in range(len(nums)-1):#0,1,2,3,4
    
#     if nums[i]<nums[i+1]:
#         total+=nums[i]
#     elif nums[i]>nums[i+1]:
#         total+=nums[i]
#         max_sum=max(total,max_sum)
#         total=0
# total+=nums[-1]
# max_sum=max(max_sum,total)
# print(max_sum)




