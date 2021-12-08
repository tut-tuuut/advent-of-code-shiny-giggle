import utils as u
import itertools

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def count_easy_letters_in_output(raw_input):
    outputs = [row.split(" | ")[1] for row in raw_input.splitlines()]
    outputs = tuple(itertools.chain(*(r.split() for r in outputs)))
    return len(tuple(filter(lambda x: len(x) in (2, 4, 3, 7), outputs)))


u.assert_equals(count_easy_letters_in_output(example_input), 26)
u.answer_part_1(count_easy_letters_in_output(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def output_sequence_from_entry(entry):
    all_sequences = tuple("".join(sorted(x)) for x in entry.split(" | ")[0].split(" "))
    outputs = tuple("".join(sorted(x)) for x in entry.split(" | ")[1].split(" "))

    one = next(x for x in all_sequences if len(x) == 2)
    four = next(x for x in all_sequences if len(x) == 4)
    seven = next(x for x in all_sequences if len(x) == 3)
    eight = next(x for x in all_sequences if len(x) == 7)

    six_characters = list(x for x in all_sequences if len(x) == 6)
    nine = next(x for x in six_characters if all(c in x for c in four))
    six_characters.remove(nine)
    zero = next(x for x in six_characters if all(c in x for c in seven))
    six_characters.remove(zero)
    six = six_characters[0]

    five_characters = list(x for x in all_sequences if len(x) == 5)
    three = next(x for x in five_characters if all(c in x for c in seven))
    five_characters.remove(three)
    top_right_segment = next(x for x in eight if x not in six)
    two = next(x for x in five_characters if top_right_segment in x)
    five = next(x for x in five_characters if top_right_segment not in x)

    values = {
        zero: "0",
        one: "1",
        two: "2",
        three: "3",
        four: "4",
        five: "5",
        six: "6",
        seven: "7",
        eight: "8",
        nine: "9",
    }
    return int("".join(values[x] for x in outputs))


def sum_output_of_sequences(raw_input):
    return sum(output_sequence_from_entry(entry) for entry in raw_input.splitlines())


example_entry = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

u.assert_equals(output_sequence_from_entry(example_entry), 5353)
u.assert_equals(sum_output_of_sequences(example_input), 61229)

u.answer_part_2(sum_output_of_sequences(raw_input))
