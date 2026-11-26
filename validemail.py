

def email(x):
    # valid=True
    for i in x:
        if i==" ":
            # valid=False
            return f' invalid email : There are white spaces in "{x}" '
        if i.isupper():
            # valid=False
            return f' invalid email : Uppercase found "{i}" , make it to lowercase'
    if "@" not in x:
        # valid=False
        return f' invalid email : @ is missing in "{x}"'
    elif not x.endswith(".com"):
        # valid=False
        return f' invalid email : "{x}" is not ending with .com'
    else:
        return "valid email"
        
a=input("Enter your email : ")    
res=email(a)
print(res)
    
    