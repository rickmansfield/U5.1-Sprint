"""- Initiate empty list/array [] 
- convert string using .split() assign to a new variable
- loop over each word in new variable 
- create conditional if word not in list[] append list with that word
- else not needed since we are not doing anyting with the duplicates other than discarding them
- convert the final list to a string using .join()
- return cleaned lists
"""
def csRemoveDuplicateWords(input_str):
    dupesRemoved = [] # O(n)
    input_str2 = input_str.split() # O(n)
    for eachWord in input_str2:
        if eachWord not in dupesRemoved: # O(n)
            dupesRemoved.append(eachWord)
            cleaned = " ".join(dupesRemoved)
    return cleaned

print(csRemoveDuplicateWords("Hi I am rick rick !"))
