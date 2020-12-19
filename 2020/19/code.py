import re

import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def generate_dict_from_raw_rules(raw_rules: str):
    return {row.split(": ")[0]: row.split(": ")[1] for row in raw_rules.splitlines()}


def generate_regex_for_rule(rule: str, rules: dict):
    if len(rule) == 3 and rule.count('"') == 2:
        return rule[1]
    if rule.count("|") == 0:
        return "".join(
            generate_regex_for_rule(rules[char], rules) for char in rule.split(" ")
        )
    if rule.count("|") > 0:
        return (
            "(?:"
            + "|".join(
                generate_regex_for_rule(subrule, rules) for subrule in rule.split(" | ")
            )
            + ")"
        )


def check_validity_for_messages(raw_input: str):
    raw_rules, raw_messages = raw_input.split("\n\n")
    ruleset = generate_dict_from_raw_rules(raw_rules)
    regex_zero = re.compile(
        "^" + generate_regex_for_rule(ruleset["0"], ruleset) + "$",
        re.MULTILINE,
    )
    return len(regex_zero.findall(raw_messages))


u.assert_equals(check_validity_for_messages(example_input), 2)
u.answer_part_1(check_validity_for_messages(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_

IMBRICATION_LEVEL = 5

raw_rules, _ = raw_input.split("\n\n")
ruleset = generate_dict_from_raw_rules(raw_rules)


def generate_regex_for_rule_part_2(rule: str, rules: dict, idx=0):
    if len(rule) == 3 and rule.count('"') == 2:
        return rule[1]
    if idx == "8" and rule == "42":
        # 8: 42 | 42 8 => 42 | 42 42 | 42 42 42…  so.. hop!  ⤵︎
        return generate_regex_for_rule_part_2("42", rules) + "+"
    if idx == "11" and rule == "42 31":
        # 11: 42 31 | 42 11 31 => 42 31 | 42 42 31 31 | 42 42 42 31 31 31…
        forty_two = generate_regex_for_rule_part_2("42", rules)
        thirty_one = generate_regex_for_rule_part_2("31", rules)
        return (
            "(?:"
            + "|".join(
                f"{forty_two*i}{thirty_one*i}" for i in range(1, IMBRICATION_LEVEL)
            )
            + ")"
        )
    if rule.count("|") == 0:
        return "".join(
            generate_regex_for_rule_part_2(rules[char], rules, char)
            for char in rule.split(" ")
        )
    if rule.count("|") > 0:
        return (
            "(?:"
            + "|".join(
                generate_regex_for_rule_part_2(subrule, rules)
                for subrule in rule.split(" | ")
            )
            + ")"
        )


def check_validity_for_messages_part_2(raw_input: str):
    raw_rules, raw_messages = raw_input.split("\n\n")
    ruleset = generate_dict_from_raw_rules(raw_rules)
    regex_zero = re.compile(
        "^" + generate_regex_for_rule_part_2(ruleset["0"], ruleset) + "$",
        re.MULTILINE,
    )
    return len(regex_zero.findall(raw_messages))


new_example = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

u.assert_equals(check_validity_for_messages_part_2(new_example), 12)

u.answer_part_2(check_validity_for_messages_part_2(raw_input))

# needed imbrication level 5 for example to work.
# it was the minimum for getting the good answer on actual input.

# result = 296 with imbrication level 5 & more
# result = 12 with imbrication level 1
# 261 with imbrication 2
# 285 with imbrication 3
# 295 with imbrication 4