"""
    practice 
    check if a string is a palindrome
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