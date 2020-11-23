import utils as u
import re
import json

with open(__file__+'.input.txt', "r+") as file:
    inputStr = file.read()

def sumOfAllNumbers(string):
    regex = r'-?\d+'
    return sum(map(int, re.findall(regex, string)))

def sumWithoutRedObjects(string):
    obj = json.loads(string)
    print(obj)
    removeRedObjects(obj)
    print(obj)

def removeRedObjects(thing):
    thingType = type(thing).__name__
    if thingType == 'list':
        print(thing)
        thing = list(filter(shouldNotBeRemoved, thing))
        print(thing)
    elif thingType == 'dict':
        for key in thing:
            if shouldNotBeRemoved(thing[key]):
                del(thing[key])

def shouldNotBeRemoved(thing):
    thingType = type(thing).__name__
    print(thing)
    if thingType == 'dict':
        for key in thing:
            if thing[key] == 'red':
                print('i should be remvoed')
                return False
        return True



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

sumWithoutRedObjects('[1,{"c":"red","b":2},3]')

# Ignore any object (and all of its children) which has any property with the value "red".
# Do this only for objects ({...}), not arrays ([...]).
# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.
