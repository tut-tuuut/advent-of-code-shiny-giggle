def required_wrapping_paper(strDimensions):
    intDimensions = list(map(int, strDimensions.split('x', 3)))
    l, w, h = intDimensions
    face1, face2, face3 = l*w, w*h, l*h
    spare = min(face1, face2, face3)
    return 2*face1 + 2*face2 + 2*face3 + spare

print('Check my code works on given examples:')
print(f"this should be 58: {required_wrapping_paper('2x3x4')}")
print(f"this should be 43: {required_wrapping_paper('1x1x10')}")

with open('input.txt', "r+") as file:
    input = file.read()

all_required_paper = sum(map(required_wrapping_paper, input.split('\n')))

print(f'The elves will need {all_required_paper} sqft of wrapping paper.')