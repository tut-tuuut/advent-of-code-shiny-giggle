import collections

# https://pymotw.com/2/collections/deque.html


def play(nb_players, last_marble):
    circle = collections.deque([0])
    scores = [0 for i in range(nb_players)]
    for new_marble in range(1, last_marble):
        if new_marble % 23 == 0:
            score = new_marble
            circle.rotate(-7)
            score += circle.pop()
            scores[new_marble % nb_players] += score
        else:
            circle.rotate(2)
            circle.append(new_marble)
    return max(scores)


print("PART 1: " + str(play(429, 70901)))
print("PART 2: " + str(play(429, 7090100)))
