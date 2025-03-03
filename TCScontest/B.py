def parse_board(input_lines):
    board = [line.split() for line in input_lines]
    start, end = None, None
    snakes = {}
    ladders = {}

    for row in board:
        for token in row:
            if token == "Start":
                start = (9, 0)
            elif token == "End":
                end = (0, 9)
            elif token.startswith("S("):
                pos = int(token[2:-1])
                snakes[pos] = True
            elif token.startswith("L("):
                pos = int(token[2:-1])
                ladders[pos] = True

    return start, end, snakes, ladders


def can_reach_end(start, end, snakes, ladders, die_inputs):
    def dfs(curr_pos, depth, snake_count, ladder_count):
        if curr_pos == end:
            return True, snake_count, ladder_count

        if depth >= len(die_inputs):
            return False, snake_count, ladder_count

        x, y = curr_pos
        next_pos = None
        for i in range(1, die_inputs[depth] + 1):
            if i == die_inputs[depth]:
                if (x + i) < 10:
                    next_pos = (x + i, y)
                else:
                    diff = (x + i) - 10
                    if y % 2 == 0:
                        next_pos = (9 - diff, y + 1)
                    else:
                        next_pos = (diff, y + 1)
                if next_pos in snakes:
                    snake_count += 1
                if next_pos in ladders:
                    ladder_count += 1

                result, snake_count, ladder_count = dfs(next_pos, depth + 1, snake_count, ladder_count)
                if result:
                    return True, snake_count, ladder_count

        return False, snake_count, ladder_count

    result, snake_count, ladder_count = dfs(start, 0, 0, 0)
    if result:
        return "Possible", snake_count, ladder_count
    else:
        return "Not possible", snake_count, ladder_count


input_lines = [
    "End S(Start) 98 97 96 95 94 93 92 91",
    "81 82 83 84 L(98) 86 87 88 89 90",
    "80 79 S(46) 77 76 75 74 73 72 71",
    "61 62 63 64 65 66 67 68 69 70",
    "60 59 58 57 56 55 S(25) 53 52 51",
    "41 42 43 L(62) 45 46 47 48 49 50",
    "40 39 38 37 36 35 34 33 32 31",
    "21 22 23 L(74) 25 26 27 28 29 30",
    "20 19 18 17 S(2) 15 14 13 12 11",
    "Start 2 3 4 5 6 7 8 9 10",
]
die_inputs = [5, 4, 2, 4, 1]

start, end, snakes, ladders = parse_board(input_lines)
result, snake_count, ladder_count = can_reach_end(start, end, snakes, ladders, die_inputs)

print(result, snake_count, ladder_count)
