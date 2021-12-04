import utils as u

with open(__file__ + ".input.txt", "r+") as file:
    raw_input = file.read()

example_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
# part 1 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_


def extract_board_from_input(raw_input):
    rows = raw_input.splitlines()
    numbers = [int(s) for s in rows.pop(0).split(",")]
    # marquer une case = inscrire -1 à la place
    new_board = False
    boards = []
    current_board = []
    for row in rows:
        if row == "":
            new_board = True
            continue
        if new_board:
            if len(current_board):
                boards.append(current_board)
            current_board = []
            new_board = False
        current_board.append([int(s) for s in filter(None, row.split(" "))])
    boards.append(current_board)
    return numbers, boards


def is_winning(board):
    return any(all(x == "x" for x in row) for row in board) or any(
        all(row[j] == "x" for row in board) for j in range(len(board[0]))
    )


losing_board = [
    [14, "x", 17, 24, 4],
    ["x", 16, 15, 9, 19],
    [18, 8, 23, "x", 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, "x", 7],
]
winning_row = [
    [14, 21, 17, 24, 4],
    ["x", "x", "x", "x", "x"],
    [18, 8, 23, 26, 20],
    [22, 11, 13, 6, 5],
    [2, 0, 12, 3, 7],
]
winning_col = [
    ["x", 21, 17, 24, 4],
    ["x", 16, 15, 9, 19],
    ["x", 8, 23, 26, 20],
    ["x", 11, 13, 6, 5],
    ["x", 0, 12, 3, 7],
]

u.assert_equals(is_winning(losing_board), False, "- losing board")
u.assert_equals(is_winning(winning_row), True, "- winning row")
u.assert_equals(is_winning(winning_col), True, "- winning col")


def debug_board(board):
    print("┌───┬───┬───┬───┬───┐")
    for row in board:
        print("│" + "│".join(f"{n:^3}" for n in row) + "│")
    print("└───┴───┴───┴───┴───┘")


def part_1(raw_input):
    numbers, boards = extract_board_from_input(raw_input)
    for drawed_number in numbers:
        boards = [
            [["x" if n == drawed_number else n for n in row] for row in b]
            for b in boards
        ]
        winning_boards = list(filter(is_winning, boards))
        if len(winning_boards):
            winning_board = winning_boards[0]
            debug_board(winning_board)
            return drawed_number * sum(
                sum(n if n != "x" else 0 for n in row) for row in winning_board
            )


u.assert_equals(part_1(example_input), 4512)
u.answer_part_1(part_1(raw_input))

# part 2 -'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,__,.-'*'-.,_
