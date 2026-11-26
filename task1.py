# a='babbabcdef'
# newa=""
# longest=0
# for i in a:
#     newa+=i
#     if newa[::-1]==newa:
#         longest=max(len(newa),longest)
# print(a[:longest])      

# def removespecialschars(s):
#     a=''
#     for i in s:
#         if i.isdigit() or i.isalpha():
#             a+=i
#     return a
# a='a@1#b'
# print(removespecialschars(a))

strs="one two three four".split()
for i in range(len(strs)):
    if i %2 !=0:
        strs[i]=strs[i][::-1]
print(" ".join(strs))        




        
  
