# Unit 5.1 Task 6

## csCheckPalindrome Complexity Defense

```python
def csCheckPalindrome(input_str):
    opposite = "".join(reversed(input_str))
    if opposite == input_str:
        return True
    else:
        return False


print(csCheckPalindrome("Love Lambda"))
print(csCheckPalindrome("mom"))
```
This code is highly efficient. "opposite" resolves to O(n) for time complexity as reversed() iterates over the string and therefore the larger the sting the longer it would take. The space complexity is O(1) as it is coverted in space to a string one time. Since these are the most significant cost for Time and Space complexity and dictate the blocks efficiency 