```python
def csReverseString(chars):
    convertedList = list()
    for eachLetter in reversed(chars):
        convertedList.append(eachLetter)
            
    return convertedList
```

The code above has a linear O(n) due to the for loop. It is the most significant cost in time complexity and therefore it is the limiting facotor. Space complexity is also O(n) since the larger the string the more space needed to accomodate the string. This block of code is as efficient as I'm capable of producing. However, as I understand it there are solutions that utilize providing space "doubling" when needed and this cleverly could reduce the space complexity to Log(n). 