import utils as u
import re

def findWinner(s, runDuration):
    regex = """(?P<name>\w+)
    [^\d]+
    (?P<v>\d+) # v = velocity
    \skm/s\s for\s
    (?P<tf>\d+) # tf = time to fly
    [^\d]+
    (?P<tr>\d+) # tr = time to rest
    \sseconds?\."""
    pattern = re.compile(regex, re.X|re.M)
    maxDistance = 0
    for row in pattern.findall(s):
        name,v,tf,tr = row
        km = calculateNbOfKm(v, tf, tr, runDuration)
        if km > maxDistance:
            maxDistance = km
    return maxDistance

def calculateNbOfKm(v,tf,tr,runDuration):
    tf = int(tf) # flying time
    tr = int(tr) # rest time
    v = int(v) # velocity
    nbOfCycles = runDuration//(tf + tr)
    flyingSecondsOnLastCycle = min(tf, runDuration%(tf + tr))
    km = v*tf*nbOfCycles + v*flyingSecondsOnLastCycle
    return km


inputStr = """Vixen can fly 8 km/s for 8 seconds, but then must rest for 53 seconds.
Blitzen can fly 13 km/s for 4 seconds, but then must rest for 49 seconds.
Rudolph can fly 20 km/s for 7 seconds, but then must rest for 132 seconds.
Cupid can fly 12 km/s for 4 seconds, but then must rest for 43 seconds.
Donner can fly 9 km/s for 5 seconds, but then must rest for 38 seconds.
Dasher can fly 10 km/s for 4 seconds, but then must rest for 37 seconds.
Comet can fly 3 km/s for 37 seconds, but then must rest for 76 seconds.
Prancer can fly 9 km/s for 12 seconds, but then must rest for 97 seconds.
Dancer can fly 37 km/s for 1 seconds, but then must rest for 36 seconds."""

exampleStr = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

u.assert_equals(findWinner(exampleStr, 1000), 1120)

u.answer_part_1(findWinner(inputStr, 2503))