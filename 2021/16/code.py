import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

examples = {
    "8A004A801A8002F478": 16,
    "620080001611562C8802118E34": 12,
    "C0015000016115A2E0802F182340": 23,
    "A0016C880162017C3686B18A3D4780": 31,
}
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def convert_hexa_string_to_bits(hex_string):
    return "".join(bin(int(char, base=16))[2:].rjust(4, "0") for char in hex_string)


u.assert_equals(
    convert_hexa_string_to_bits("EE00D40C823060"),
    "11101110000000001101010000001100100000100011000001100000",
)

u.assert_equals(convert_hexa_string_to_bits("D2FE28"), "110100101111111000101000")

TYPE_LITERAL_VALUE = 4


def part_1(hex_input):
    bits = convert_hexa_string_to_bits(hex_input)
    print(bits)
    version_number = int(bits[:3], base=2)
    type_id = int(bits[3:6], base=2)
    if type_id == TYPE_LITERAL_VALUE:
        index = 6
        value_bits = []
        last_group = False
        while last_group == False:
            group = bits[index : index + 5]
            value_bits.append(group[1:])
            index += 5
            last_group = group[0] == "0"
        result = int("".join(value_bits), base=2)
    else:
        length_type_id = bits[6]
        if length_type_id == "0":
            print("length type id 0")
            sub_packet_length = int(bits[7 : 7 + 15], base=2)
            sub_packets = bits[22 : 22 + sub_packet_length]
            print("sub packets", sub_packets)
            sub_packets_result = part_1(sub_packets)


part_1("D2FE28")
part_1("38006F45291200")
# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
