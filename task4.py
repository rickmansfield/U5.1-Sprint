"""
# import builtins
print(dir(builtins))
print(dir(reversed))
print(help(reversed))
print(help(next))
- Initiate a variable to hold the reversed() and join() version of the submitted variable. 
- create simple conditional to compare original to reversed orders and return True/False respectively
    
"""

def csCheckPalindrome(input_str): # Time O(n) space O(1) 
    opposite = "".join(reversed(input_str))
    if opposite == input_str:
        return True
    else:
        return False


print(csCheckPalindrome("Love Lambda"))
print(csCheckPalindrome("mom"))