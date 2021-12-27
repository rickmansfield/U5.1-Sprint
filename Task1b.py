"""
initiate new list []
loop over given list in reverse order 
append new list with each char
retrun reversed list
additional resources https://realpython.com/reverse-string-python/#reversing-strings-with-core-python-tools
https://realpython.com/python-reverse-list/#reversing-lists-in-place

"""
# print(help(reversed))

def csReverseString(chars): # time O(n) Space O(n) ie. both linear
    convertedList = list()
    for eachLetter in reversed(chars):
        convertedList.append(eachLetter)
            
    return convertedList

print(csReverseString("Love Lambda"))