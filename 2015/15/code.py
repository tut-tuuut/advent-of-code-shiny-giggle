import utils as u
import math
import re

def dot(v,w): # "produit scalaire" in French
    return sum([a*b for (a,b) in zip(v,w)])

constraints = ( # i parsed it with my own eyes and brain
    ( 5, -1, 0, -1), # capacity
    (-1,  3, -1, 0), # durability
    ( 0,  0,  4, 0), # flavor
    ( 0,  0,  0, 2), # texture
)
caloriesVector = (5, 1, 6, 8)


size = 100 # 156 849 iterations for size 100
generator = ((x,y,z,size-x-y-z) for x in range(1, size) for y in range(1, size - x) for z in range(1,size-x-y))
maxScore = 0
maxScores500Calories = 0
for row in generator:
    score = math.prod([max(0, dot(constraint, row)) for constraint in constraints])
    calories = dot(row, caloriesVector)
    if (score > maxScore):
        maxScore = score
    if (calories == 500 and score > maxScores500Calories):
        maxScores500Calories = score
    #print(f'\033[91m'+'a'*row[0]+'\033[92m'+'b'*row[1]+'\033[94m'+'c'*row[2]+'\033[93m'+'d'*row[3]+f'\033[0m {score}')

u.answer_part_1(maxScore)
u.answer_part_2(maxScores500Calories)
