import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def hash_string(str):
    current_value = 0
    for c in str:
        current_value += ord(c)
        current_value = (current_value * 17) % 256
    return current_value


u.assert_equal(hash_string("HASH"), 52)
u.assert_equal(hash_string("pc=6"), 214)


def part_1(raw_input):
    return sum(hash_string(str) for str in raw_input.strip().split(","))


u.assert_equal(part_1("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"), 1320)

u.answer_part_1(part_1(raw_input))

# 514435 too high, i needed to strip() my raw input first

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def part_2(raw_input):
    init_sequence = raw_input.strip().split(",")
    boxes = dict()
    for instruction in init_sequence:
        # print("----")
        # print(instruction)
        if "=" in instruction:
            label, value = instruction.split("=")
            box_id = hash_string(label)
            box = boxes.get(box_id, dict())
            box[label] = value
            boxes[box_id] = box
            # print(label, value)
        elif "-" in instruction:
            label = instruction[:-1]
            box_id = hash_string(label)
            box = boxes.get(box_id, dict())
            if label in box:
                del box[label]
            boxes[box_id] = box
            # print(label)
    # print(boxes)
    result_sum = 0
    for box_id, box in boxes.items():
        for slot_number, lensvalue in enumerate(box.values()):
            # print( box_id+1, slot_number+1, lensvalue)
            result_sum += (box_id + 1) * (slot_number + 1) * int(lensvalue)
    return result_sum


u.assert_equal(part_2("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"), 145)

u.answer_part_2(part_2(raw_input))
