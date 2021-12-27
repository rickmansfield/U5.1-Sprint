def removeDupes(s):
    splitString = s.split()
    result = []
    for eachWord in splitString:
        if eachWord not in result:
            result.append(eachWord)
    return " ".join(result)
    
print(removeDupes('hi hi hello'))
print(removeDupes("Hi I am rick rick !"))