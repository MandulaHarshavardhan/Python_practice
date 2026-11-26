def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=arr[:mid]
    right_half=arr[mid:]
    left_half=merge_sort(left_half)
    right_half=merge_sort(right_half)
    return merge_arrays(left_half,right_half)


def merge_arrays(arr1,arr2):
    res=[]
    i,j=0,0
    m=len(arr1)
    n=len(arr2)
    while i<m and j<n:
        if arr1[i]<=arr2[j]:
            res.append(arr1[i])
            i+=1
        else:
            res.append(arr2[j])
            j+=1
    if i<m:
        while i<m:
            res.append(arr1[i])
            i+=1
    if j<n:
        while j<n:
            res.append(arr2[j])
            j+=1
    return res

# left=[1,2,3,4]
# right=[1,1,3,4,5,6,7]
nums=[3,1,6,2,4,8,7]
print(merge_sort(nums))