"""
"""


def csReverseString(chars):
    reversedList = reversed(chars)
    newFullyReversedList = "".join(reversedList)
    return newFullyReversedList


print(csReverseString("Love Lambda"))


def csReverseString2(chars):
    newFullyReversedList = "".join(reversed(chars))
    return newFullyReversedList


print(csReverseString2("Love Lambda"))


def csReverseString3(chars):
    return "".join(reversed(chars))


print(csReverseString3("Love Lambda"))
