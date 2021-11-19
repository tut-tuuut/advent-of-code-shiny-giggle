import utils as u
import re
import json

with open(__file__ + ".input.txt", "r+") as file:
    inputStr = file.read()


def sumOfAllNumbers(string):
    regex = r"-?\d+"
    return sum(map(int, re.findall(regex, string)))


def removeRedObjects(s):
    objectsWithoutChildren = r"\{[^\{\}]*\}"
    # \{        an opening moustache,
    # [^\{\}]*  some characters which are not moustaches,
    # \}        a closing moustache
    redObjects = r'\{[^\{\}]*\:"red"[^\{\}]*\}'
    # \{        an opening moustache,
    # [^\{\}]*  some characters which are not moustaches,
    # \:"red"   the string :"red",
    # [^\{\}]*  some non-moustache characters again
    # \}        a closing moustache

    i = 0
    while len(re.findall(objectsWithoutChildren, s)) > 0:
        i = i + 1
        print(f"iteration {i} length {len(s)}")
        while len(re.findall(redObjects, s)) > 0:
            print(f"remove {len(re.findall(redObjects, s))} red objects")
            s = re.sub(redObjects, "> 0 <", s)
        print(f"factorize {len(re.findall(objectsWithoutChildren, s))} non red objects")
        s = re.sub(
            objectsWithoutChildren, lambda x: f"> {sumOfAllNumbers(x.group(0))} <", s
        )
        print("--------")

    # print(string)
    return s


# [1,2,3] and {"a":2,"b":4} both have a sum of 6
u.assert_equals(sumOfAllNumbers("[1,2,3]"), 6)
u.assert_equals(sumOfAllNumbers('{"a":2,"b":4}'), 6)

# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
u.assert_equals(sumOfAllNumbers("[[[3]]]"), 3)
u.assert_equals(sumOfAllNumbers('{"a":{"b":4},"c":-1}'), 3)

# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
u.assert_equals(sumOfAllNumbers('{"a":[-1,1]}'), 0)
u.assert_equals(sumOfAllNumbers('[-1,{"a":1}]'), 0)

# [] and {} both have a sum of 0.
u.assert_equals(sumOfAllNumbers("[]"), 0)
u.assert_equals(sumOfAllNumbers(r"{}"), 0)

u.answer_part_1(sumOfAllNumbers(inputStr))

u.assert_equals(4, sumOfAllNumbers(removeRedObjects('[1,{"c":"red","b":2},3]')))
u.assert_equals(sumOfAllNumbers(removeRedObjects('{"d":"red","e":[1,2,3,4],"f":5}')), 0)

inputStrWithoutRed = removeRedObjects(inputStr)
u.answer_part_2(sumOfAllNumbers(inputStrWithoutRed))
# part2 85717 too high
# part2 68466 yay!

# Ignore any object (and all of its children) which has any property with the value "red".
# Do this only for objects ({...}), not arrays ([...]).
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.
