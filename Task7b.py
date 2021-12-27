def removeDupes(s):
    arrayOfWords = s.split() ## creates an array of words
    noDupes = []
    for eachWord in arrayOfWords:
        if eachWord not in noDupes:
            noDupes.append(eachWord)
    return " ".join(noDupes)
    
print(removeDupes('hi hi hello'))
print(removeDupes("Hi I am rick rick !"))