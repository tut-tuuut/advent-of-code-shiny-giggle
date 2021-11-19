import re

# what is the number of characters of code for string literals
# minus
# the number of characters in memory for the values of the strings in total for the entire file?

"""
    "" is 2 characters of code (the two double quotes), but the string contains zero characters.
    "abc" is 5 characters of code, but 3 characters in the string data.
    "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
    "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
"""

"""
For example, given the four strings above,
the total number of characters of string code (2 + 5 + 10 + 6 = 23)
minus
the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11)
is 23 - 11 = 12.
"""


def getDifferenceBetweenCodeAndResult(string):
    initialLength = len(string)

    # remove leading and trailing " on each line
    string = re.sub(r'^"', "", string, flags=re.MULTILINE)
    string = re.sub(r'"$', "", string, flags=re.MULTILINE)

    # escaped \\ and \" add 1 to the difference
    string = string.replace("\\\\", "S")
    string = string.replace('\\"', "T")
    string = re.sub(r"\\x[a-f0-9]{2}", "U", string)
    # print(string)
    return initialLength - len(string)


def getDifferenceResultAndCode(string):
    initialLength = len(string)

    # leading and trailing " each result in 3 characters in resulting string
    string = re.sub(r'^"', "mmm", string, flags=re.MULTILINE)
    string = re.sub(r'"$', "mmm", string, flags=re.MULTILINE)

    # escape \ and "
    string = string.replace("\\", "SS")
    string = string.replace('"', "TT")

    return initialLength - len(string)


with open(__file__ + ".input.example.txt", "r+") as file:
    inputStr = file.read()
    print("this should be 12:")
    print(getDifferenceBetweenCodeAndResult(inputStr))

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()
    print("this is answer to part 1:")
    print(getDifferenceBetweenCodeAndResult(inputStr))
    print("this is answer to part 2:")
    print(getDifferenceResultAndCode(inputStr))
    # 1349 is too high
    # 1340 too
    # 972 is too low
