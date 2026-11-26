nums = [2, 4, 6, 8, 10, 12, 14]
target = 10
def binarysearch(nums,target):
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if nums[mid]==target:
            return mid
        elif target<nums[mid]:
            right=mid-1
        elif target>nums[mid]:
            left=mid+1
    return -1
print(binarysearch(nums,target))