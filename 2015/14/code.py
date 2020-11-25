import utils as u
import re

def findWinnerPart1(s, runDuration):
    maxDistance = 0
    for row in parseInputStr(s):
        name,v,tf,tr = row
        km = calculateNbOfKm(v, tf, tr, runDuration)
        if km > maxDistance:
            maxDistance = km
    return maxDistance

def findWinnerPart2(s, runDuration):
    scores = dict()
    reindeers = dict()
    for row in parseInputStr(s):
        name,v,tf,tr = row
        scores[name] = 0
        reindeers[name] = (int(v), int(tf), int(tr))
    for i in range(1,runDuration):
        maxDistance = 0
        aheadReindeers = []
        for name in reindeers: # calculate position of every reindeer at that time
            distance = calculateNbOfKm(*reindeers[name],i)
            if distance > maxDistance:
                maxDistance = distance
                aheadReindeers = [name]
            elif distance == maxDistance:
                aheadReindeers.append(name)
        for name in aheadReindeers: # update scores
            scores[name] = scores[name] + 1
    return max(scores.values())
            
def calculateNbOfKm(v,tf,tr,runDuration):
    tf = int(tf) # flying time
    tr = int(tr) # rest time
    v = int(v) # velocity
    nbOfCycles = runDuration//(tf + tr)
    flyingSecondsOnLastCycle = min(tf, runDuration%(tf + tr))
    km = v*tf*nbOfCycles + v*flyingSecondsOnLastCycle
    return km

def parseInputStr(s):
    regex = """(?P<name>\w+)
    [^\d]+
    (?P<v>\d+) # v = velocity
    \skm/s\s for\s
    (?P<tf>\d+) # tf = time to fly
    [^\d]+
    (?P<tr>\d+) # tr = time to rest
    \sseconds?\."""
    pattern = re.compile(regex, re.X|re.M)
    for row in pattern.findall(s):
        yield row

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

u.assert_equals(findWinnerPart1(exampleStr, 1000), 1120)
u.answer_part_1(findWinnerPart1(inputStr, 2503))

u.assert_equals(findWinnerPart2(exampleStr, 1000), 689)
u.answer_part_2(findWinnerPart2(inputStr, 2503))
