"""
WARNING this solution works in real life but does not
meet codesignal requirements. See /Taks1.b for
the passing solution. 
    """
# import builtins
# print(dir(builtins))
# print(dir(reversed))
# print(help(reversed))
# print(help(next))


def reverseString(str):
    backwards = reversed(str)
    # print(next(backwards))
    # print(next(backwards))
    # print(next(backwards))
    return "".join(backwards)

print(reverseString("Love Lambda"))
