def palindromecheck(func):
    def wrapper(s):
        if s==s[::-1]:
            print("palindrome !")
        else:
            print("Not a palindrome !")
        return func(s)
    return wrapper


@palindromecheck
def ispalindrome(s):
    print("checking : ",s)
a=ispalindrome("Harsha")