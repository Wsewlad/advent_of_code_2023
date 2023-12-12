import pandas as pd


def find_farthest_step_from_start(input_text: str) -> int:
    # (x, y)
    rules = {
        # "|": {(0, -1), (0, 1)},
        "|": {(-1, 0), (1, 0)},
        # "-": {(-1, 0), (1, 0)},
        "-": {(0, -1), (0, 1)},
        # "L": {(0, -1), (1, 0)},
        "L": {(-1, 0), (0, 1)},
        # "J": {(-1, 0), (0, -1)},
        "J": {(-1, 0), (0, -1)},
        # "7": {(-1, 0), (0, 1)},
        "7": {(0, -1), (1, 0)},
        # "F": {(1, 0), (0, 1)},
        "F": {(0, 1), (1, 0)},
        # "S": {(1, 0), (0, -1), (-1, 0), (0, 1)},
        "S": {(0, 1), (-1, 0), (0, -1), (1, 0)},
    }
    matrix = [[*line] for line in input_text.splitlines()]
    df = pd.DataFrame(matrix)
    start = df[df == "S"].stack().index.tolist()[0]
    steps = [start]
    visited = set()
    steps_count: int = 0
    while steps:
        (y, x) = steps.pop(0)
        if (y, x) in visited:
            break
        visited.add((y, x))
        steps_count += 1
        # print(matrix[y][x])
        for dy, dx in rules.get(matrix[y][x], set()):
            if 0 <= y + dy < len(matrix) and 0 <= x + dx < len(matrix[0]) and matrix[y + dy][x + dx] != ".":
                rules_to_check = rules.get(matrix[y + dy][x + dx])
                if (-dy, -dx) in rules_to_check and (y + dy, x + dx) not in visited:
                    steps.append((y + dy, x + dx))
                    break
    result = int(steps_count / 2)
    print(result)
    return int(steps_count / 2)


sample1 = """.....
.S-7.
.|.|.
.L-J.
.....
"""

sample2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

assert find_farthest_step_from_start(sample1) == 4
assert find_farthest_step_from_start(sample2) == 8
with open("input.txt") as f:
    input_text = f.read()
    find_farthest_step_from_start(input_text)
