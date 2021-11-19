import re
import unittest

# import django
# import networkx as nx

import utils as u

# from . import utils as u # <3

# PEP8 = bien ! Ultra adopté dans la commu Python
# = signe ++ de qualité
# snake_case fonctions et variables
# CamelCase pour les classes
# autopep8 = te crie dessus si tu ne fais pas le boulot à ta place
# possibilité d'ajouter des annotations de type

# pep8 => dit comment ordonner les import en 3 groupes
# 1. lib standard
# 2. paquets installés
# 3. ma codebase
# Vérifiable avec isort

# NameError: name 's' is not defined
def find_winner_part_1(s: str, runDuration: int) -> int:
    return max(
        calculateNbOfKm(v, tf, tr, runDuration) for name, v, tf, tr in parseInputStr(s)
    )


def find_winner_part_1(s: str, runDuration: int) -> int:
    return max(
        calculateNbOfKm(*rest, tr, runDuration) for _, *rest, tr in parseInputStr(s)
    )


# dict() : non. (Bon c'est pas trop grave mais c'est pas la peine.)
def findWinnerPart2(s, runDuration):
    from collections import defaultdict  # import scopé à la fonction

    scores = defaultdict(int)
    reindeers = {}
    for row in parseInputStr(s):
        name, v, tf, tr = row
        # scores[name] = 0
        reindeers[name] = (int(v), int(tf), int(tr))
    for i in range(1, runDuration):
        maxDistance = 0
        # aheadReindeers = []
        for name in reindeers:  # calculate position of every reindeer at that time
            distance = calculateNbOfKm(*reindeers[name], i)
            if distance > maxDistance:
                maxDistance = distance
                aheadReindeers = [name]
            elif distance == maxDistance:
                aheadReindeers.append(name)
        for name in aheadReindeers:  # update scores
            scores[name] += 1
    return max(scores.values())


# a * b -> a.__mul__(b)
# a * b -> b.__rmul__(a)
# class int:
# def __mul__(self, other):

# collections, bien pour
# namedTuple
# defaultDict
# deque double ended queue (pour les files et les piles)
# counter : pour compter des trucs

# operator.attrgetter(attr)
# operator.attrgetter(*attrs)
# cool pour récupérer des attributs sous forme de tuples
# cool aussi en combinaison avec les fonctions de tri
#


def calculateNbOfKm(v, tf, tr, runDuration):
    tf = int(tf)  # flying time
    tr = int(tr)  # rest time
    v = int(v)  # velocity
    nbOfCycles = runDuration // (tf + tr)
    flyingSecondsOnLastCycle = min(tf, runDuration % (tf + tr))
    km = v * tf * nbOfCycles + v * flyingSecondsOnLastCycle
    return km


def parseInputStr(s):
    # foo = 'event "%s" happened' % (event_name,)
    # logging.warn('event "%s" happened', event_name, )
    # output = _('Today is %(month)s %(day)s.') % {'month': m, 'day': d}
    regex = r"""(?P<name>\w+)
    [^\d]+
    (?P<v>\d+) # v = velocity
    \skm/s\s for\s
    (?P<tf>\d+) # tf = time to fly
    [^\d]+
    (?P<tr>\d+) # tr = time to rest
    \sseconds?\."""
    pattern = re.compile(regex, re.X | re.M)

    for row in pattern.findall(s):
        yield ()


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


u.assert_equals(find_winner_part_1(exampleStr, 1000), 1120)
u.answer_part_1(find_winner_part_1(inputStr, 2503))


u.assert_equals(findWinnerPart2(exampleStr, 1000), 689)
u.answer_part_2(findWinnerPart2(inputStr, 2503))

# /usr/local/bin/python3 /Users/ahr/Code/advent-of-code-shiny-giggle/2015/14/code.py
# python3 -m unittest 2015/14/code.py


class CdiscountTestCase(unittest.TestCase):
    pass


class CasinoTestCase(unittest.TestCase):
    pass


# help(code.TestFoo)
# code.TestFoo.mro()d
class TestFoo(CdiscountTestCase, CasinoTestCase):
    "Une classe qui teste"

    def test_bar(self):
        "une fonction qui teste"
        self.assertEqual(find_winner_part_1(exampleStr, 1000), 1120)
        foo = """
        lolilol
        """


# pytest ou py.test # <3
def test_examples_part_1():
    assert find_winner_part_1(exampleStr, 1000) == 1120, "ça a pas marché"
    assert len(ma_liste) == 12
