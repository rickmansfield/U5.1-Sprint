```python
def csRemoveDuplicateWords(str):
    dupesRemoved = []
    str2 = str.split()
    for eachWord in str2: #O(n)
        if eachWord not in dupesRemoved:
            dupesRemoved.append(eachWord)
            cleaned = " ".join(dupesRemoved)
    return cleaned
```

The code above uses a loop which causes a time complexity of O(n) it is the most significant time complexty and therefore the entire block is linear in time complextiy. The larger the input the longer it will take to process. The space complexity is O(n) becuase as the input grows the space required also grows. However as I understand it there are fail safes in place to convert the O(n) to Log(n) using a doubling of space which would eventually reduce the space complexity problem. Nonetheless, again there is likely little to know other ways to improve "significantly" on this linear process. Real world alternatives might include some cleaver throttles to the size of submission of data or warnings to the user that larger submissions would require longer processing times. 