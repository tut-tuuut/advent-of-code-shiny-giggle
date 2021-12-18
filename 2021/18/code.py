import re
import utils as u


class SnailfishNb:
    def __init__(self, description, level=0, parent=None):
        self.level = level
        self.parent = parent
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

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
