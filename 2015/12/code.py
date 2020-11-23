import utils as u
import re
import json

with open(__file__+'.input.txt', "r+") as file:
    inputStr = file.read()

def sumOfAllNumbers(string):
    regex = r'-?\d+'
    return sum(map(int, re.findall(regex, string)))

# [1,2,3] and {"a":2,"b":4} both have a sum of 6
u.assert_equals(sumOfAllNumbers('[1,2,3]'), 6)
u.assert_equals(sumOfAllNumbers('{"a":2,"b":4}'), 6)

# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
u.assert_equals(sumOfAllNumbers('[[[3]]]'), 3)
u.assert_equals(sumOfAllNumbers('{"a":{"b":4},"c":-1}'), 3)

# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
u.assert_equals(sumOfAllNumbers('{"a":[-1,1]}'), 0)
u.assert_equals(sumOfAllNumbers('[-1,{"a":1}]'), 0)

# [] and {} both have a sum of 0.
u.assert_equals(sumOfAllNumbers('[]'), 0)
u.assert_equals(sumOfAllNumbers(r'{}'), 0)

u.answer_part_1(sumOfAllNumbers(inputStr))