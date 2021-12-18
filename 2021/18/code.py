import re
from math import floor, ceil
import utils as u


class SnailfishNb:
    def __init__(self, description, level=0, parent=None):
        self.level = level
        self.parent = parent
        self.exploded = False
        if re.match(r"\[\d+,\d+\]", description):
            self.left, self.right = map(int, description[1:-1].split(","))
            return
        description = description[1:-1]
        for comma in re.finditer(",", description):
            half_string = description[comma.start() :]
            if half_string.count("]") == half_string.count("["):
                left_string = description[: comma.start()]
                right_string = description[comma.end() :]
                if left_string.isnumeric():
                    self.left = int(left_string)
                else:
                    self.left = SnailfishNb(
                        left_string, level=self.level + 1, parent=self
                    )
                if right_string.isnumeric():
                    self.right = int(right_string)
                else:
                    self.right = SnailfishNb(
                        right_string, level=self.level + 1, parent=self
                    )

    def __str__(self):
        return f"[{self.left},{self.right}]"

    def __add__(self, other):
        result = SnailfishNb("")
        self.increase_level()
        other.increase_level()
        self.parent = result
        other.parent = result
        result.left = self
        result.right = other
        return result

    def increase_level(self):
        self.level += 1
        if isinstance(self.left, self.__class__):
            self.left.increase_level()
        if isinstance(self.right, self.__class__):
            self.right.increase_level()

    def is_two_regulars(self):
        return isinstance(self.left, int) and isinstance(self.right, int)

    def is_regular_left(self):
        return isinstance(self.left, int)

    def is_regular_right(self):
        return isinstance(self.right, int)

    def reduce(self):
        if self.is_two_regulars() and self.level >= 4:
            self.explode()
            return True
        if self.is_regular_left():
            if self.left >= 10:
                description = f"[{floor(self.left/2)},{ceil(self.left/2)}]"
                self.left = SnailfishNb(description, level=self.level + 1, parent=self)
                return True
        if self.is_regular_right():
            if self.right >= 10:
                description = f"[{floor(self.right/2)},{ceil(self.right/2)}]"
                self.right = SnailfishNb(description, level=self.level + 1, parent=self)
                return True
        if not self.is_regular_left() and self.left.reduce():
            if self.left.exploded:
                self.left = 0
            return True
        if not self.is_regular_right() and self.right.reduce():
            if self.right.exploded:
                self.right = 0
            return True
        return False

    def explode(self):
        self.parent.add_on_left(self.left)
        self.parent.add_on_right(self.right)
        self.exploded = True

    def add_on_left(self, value):
        if self.is_regular_left():
            self.left += value
        elif self.parent is not None:
            self.parent.add_on_left(value)

    def add_on_right(self, value):
        if self.is_regular_right():
            self.right += value
        elif self.parent is not None:
            self.parent.add_on_right(value)


examples = """[1,2]
[[1,2],3]
[9,[8,7]]
[[1,9],[8,5]]
[[[[1,2],[3,4]],[[5,6],[7,8]]],9]
[[[9,[3,8]],[[0,9],6]],[[[3,7],[4,9]],3]]
[[[[1,3],[5,3]],[[1,3],[8,7]]],[[[4,9],[6,9]],[[8,2],[7,3]]]]"""

u.pink("-'*'-.,__,.-'*'-( parsing and __str__ tests )-'*'-.,__,.-'*'-")
for x in examples.splitlines():
    u.assert_equals(str(SnailfishNb(x)), x)

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

u.pink("-'*'-.,__,.-'*'-( simple __add__ test )-'*'-.,__,.-'*'-")

result = SnailfishNb("[1,2]") + SnailfishNb("[[3,4],5]")
u.assert_equals(str(result), "[[1,2],[[3,4],5]]")
u.assert_equals(result.level, 0)
u.assert_equals(result.left.parent, result)
u.assert_equals(result.left.level, 1)
u.assert_equals(result.right.parent, result)
u.assert_equals(result.right.level, 1)
u.assert_equals(result.right.left.level, 2)

u.pink("-'*'-.,__,.-'*'-( explode tests )-'*'-.,__,.-'*'-")

explode_examples = (
    ("[[[[[9,8],1],2],3],4]", "[[[[0,9],2],3],4]"),
    ("[7,[6,[5,[4,[3,2]]]]]", "[7,[6,[5,[7,0]]]]"),
    ("[[6,[5,[4,[3,2]]]],1]", "[[6,[5,[7,0]]],3]"),
    ("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"),
    ("[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]", "[[3,[2,[8,0]]],[9,[5,[7,0]]]]"),
)

for before, after in explode_examples:
    nb = SnailfishNb(before)
    nb.reduce()
    u.assert_equals(str(nb), after)

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
