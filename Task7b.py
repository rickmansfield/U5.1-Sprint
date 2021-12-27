def removeDupes(s):
    arrayOfWords = s.split() ## creates an array of words from the given string "s".
    noDupes = []
    for eachWord in arrayOfWords:
        if eachWord not in noDupes:
            noDupes.append(eachWord)
    return " ".join(noDupes) ## returns converted array into a string with spaces inbetween each word
    
print(removeDupes('hi hi hello'))
print(removeDupes("Hi I am rick rick !"))