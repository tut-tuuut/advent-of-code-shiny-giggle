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
