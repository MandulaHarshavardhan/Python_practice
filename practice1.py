list1 = [1,2,4] #[1,2,4,0,0,0]
l=len(list1)
list2 = [1,3,4]
list1.extend([0]*len(list2))
r=len(list2)
x=l+r-1
i=l-1
j=r-1
while j>=0:
    if i>=0 and list1[i]>list2[j]:
        list1[x]=list1[i]
        i-=1
    else:
        list1[x]=list2[j]
        j-=1
    x-=1
print(list1)    

