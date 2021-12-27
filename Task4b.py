"""
    practice 
    write a Python Function that checks if a stringafied word is a palindrome
    """


def checkPalindrome(s):
    rev = "".join(reversed(s))
    if rev == s:
        return True
    else:
        return False
    
print(checkPalindrome('mom'))
print(checkPalindrome('bob'))
print(checkPalindrome('boob'))
print(checkPalindrome('rick'))
print(checkPalindrome("Love Lambda"))
print(checkPalindrome("saras"))
print(checkPalindrome('eye'))
print(checkPalindrome('me'))
