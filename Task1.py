    """
WARNING this solution works in real life but does not
meet codesignal requirements. See /Taks1.b for
the passing solution. 
    """
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

