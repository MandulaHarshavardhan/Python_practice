# def decfun(fun):
#     def innerfun():
#         print("="*20)
#         fun()
#         print("="*20)
#     return innerfun    
# @decfun
# def display():
#     print("Welcome to Python !")
# display()

# def toupper(fun):
#     def innerfun(x):
#         a=''
#         for i in x:
#             if i.isalpha:
#                 a=a+i.upper()
#         print(a)
#     return innerfun        

# @toupper
# def display(x):
#     print(x)
# x="Hello Batch-85"
# display(x)  


# def counts(fun):
#     def innerfun(a):
#         fun(a)
#         print(len(a))
        
#     return innerfun

# @counts
# def display(x):
#     print(x)

# a="Programming"
# display(a)    

# def outerfun():
#     suffix="ing"
#     def innerfun():
#         string="dancinga"
#         if string.endswith(suffix):
#             return True
#         else:
#             return False    
#     return innerfun()

# print(outerfun())

'''def longestword():
    sentence="level world python amazing apple"
    def unique():
        a=sentence.split()
        words=[]
        for i in a:
            if len(set(i))!=len(i):
                continue
            words.append(i)
        return max(words)
longestword() '''       



def longestuniqueword(x):
    sentence=x.split()
    longest=''
    for i in sentence:
        if len(i)==len(set(i)):
            if len(i)>len(longest):
                longest = i
    return longest
a="level world python amazing apple"
print(longestuniqueword(a))
