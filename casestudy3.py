nums=[5,3,1,6,2]
for i in range(len(nums)):
    for j in range(len(nums)):
        if i==j:
            continue
        elif nums[i]<nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
print(nums)

def counts(fun):
    count=0
    def wrapper(x):
        nonlocal count
        count+=1
        print(fun(x))
        print(f'Call Count : {count}')
    return wrapper
@counts
def display(x):
    return "Function Executed Successfully"
display(1)
display(2)
display(3)
