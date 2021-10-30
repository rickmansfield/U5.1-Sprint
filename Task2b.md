I had to solve this two times. The first time I was nervous and rushed through UPER and came up with
```python
# import builtins
# print(dir(builtins))
# print(dir(reversed))
print(help(reversed))
# print(help(next))


def reverseString(str):
    greeting = reversed(str)
    # print(next(greeting))
    # print(next(greeting))
    # print(next(greeting))
    return "".join(greeting)

print(reverseString("Love Lambda"))
```

After starting over and paying closer attention to U.P.E.R
My steps 
- save new list in a variable to converted array into a list this originates as empty. 
- use reversed() and assign a variable. 
- loop over each letter of the reversed original list
- append the list new list
- return the converted list