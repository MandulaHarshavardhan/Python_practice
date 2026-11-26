def checknum(fun):
    def innerfun(x):
        a=fun(x)
        for i in range(2,a//2+1):
            if a%i ==0 :
                print(f'Not a Prime num -> {a}')
                return
        print(f'Prime Number Accepted -> {a**2}')    
    return innerfun
@checknum
def isprime(x):#13
    return x
isprime(13)

def check(fun):
    attempts=1
    res=[]
    def innerfun():
        nonlocal attempts
        while attempts<4:
            b=input("Enter : ")
            res.append(f"attempt {attempts} : {b}")
              
            if b == "Success":
                break 
            attempts+=1 
        for i in res:
            print(i)    
    return innerfun        
@check
def display():
    return 
display()

a=input().split()
a.sort(key=lambda x:sum(ch in "aeiou" for ch in x))
for i in a:
    print(i)



def counts(x):
    if x=="":
        return 0
    if x[0]=="g":
        return 1+counts(x[1:])
    else:
        return counts(x[1:])

s="programming"
print(counts(s))

def decorator(fun):
    def wrapper():
        print("*"*20)
        fun()
        print("*"*20)
    return wrapper
@ decorator
def display():
    print("Harsha Chary")
display()      

  
    