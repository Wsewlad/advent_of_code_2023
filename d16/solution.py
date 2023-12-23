import pandas as pd


def find_direction(symb: str, current: str) -> list:
    """
    Returns a list of directions that are allowed to go from the current position
    ARGS:
        symb: symbol on the current position
        current: current direction
    RETURNS:
        list of directions
    """
    if symb == '.':
       return [current]
    elif symb == '-' and current in ['L', 'R']:
        return [current]
    elif symb == '|' and current in ['U', 'D']:
        return [current]
    elif symb == '-' and current in ['U', 'D']:
        return ['R', 'L']
    elif symb == '|' and current in ['L', 'R']:
        return ['U', 'D']
    elif symb == '/':
        if current == 'R':
            return ['U']
        elif current == 'L':
            return ['D']
        elif current == 'U':
            return ['R']
        else:
            return ['L']
    elif symb == '\\':
        if current == 'U':
            return ['L']
        elif current == 'D':
            return ['R']
        elif current == 'L':
            return ['U']
        else:
            return ['D']


def navigate_recursively(df: pd.DataFrame, current_step: tuple, direction: str, energized_set: set) -> None:
    """
    Navigates through the contraption recursively
    ARGS:
        df: contraption as a dataframe
        current_step: current position
        direction: current direction
        energized_set: set of energized positions
    RETURNS:
        None
    """
    splitters = {'|', '-'}
    rules = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    energized_set.add(current_step)
    next_step = tuple(map(sum, zip(current_step, rules[direction])))
    if (
        next_step[0] < 0
        or next_step[1] < 0
        or next_step[0] >= df.shape[1]
        or next_step[1] >= df.shape[0]
    ):
        return
    next_symb = df.iloc[next_step[1], next_step[0]]
    if next_step in energized_set and next_symb in splitters:
        return
    next_directions = find_direction(next_symb, direction)
    for next_direction in next_directions:
        navigate_recursively(df, next_step, next_direction, energized_set)


def navigate_iteratively(df: pd.DataFrame, start_step: tuple, start_direction: str, energized_set: set) -> None:
    """
    Navigates through the contraption iteratively
    ARGS:
        df: contraption as a dataframe
        start_step: start position
        start_direction: start direction
        energized_set: set of energized positions
    RETURNS:
        None
    """
    splitters = {'|', '-'}
    rules = {
        'U': (0, -1),
        'D': (0, 1),
        'R': (1, 0),
        'L': (-1, 0),
    }
    stack = [(start_step, start_direction)]
    while stack:
        current_step, direction = stack.pop()
        energized_set.add(current_step)
        next_step = tuple(map(sum, zip(current_step, rules[direction])))
        if (
            next_step[0] < 0
            or next_step[1] < 0
            or next_step[0] >= df.shape[1]
            or next_step[1] >= df.shape[0]
        ):
            continue
        next_symb = df.iloc[next_step[1], next_step[0]]
        if next_step in energized_set and next_symb in splitters:
            continue
        next_directions = find_direction(next_symb, direction)
        for next_direction in next_directions:
            stack.append((next_step, next_direction))


def find_number_of_energized_tiles(input_text: str) -> int:
    """
    Finds the number of energized tiles
    ARGS:
        input_text: input text
    RETURNS:
        number of energized tiles
    """
    energized = set()
    contraption = [[s for s in list(line)] for line in input_text.splitlines()]
    df = pd.DataFrame(contraption)
    start = (0, 0)
    direction = find_direction(df.iloc[start[1], start[0]], 'R')[0]
    navigate_iteratively(df, start, direction, energized)
    return len(energized)


def find_number_of_energized_tiles_starting_from_each_border_point(input_text: str) -> int:
    """
    Finds the number of energized tiles starting from each border point
    ARGS:
        input_text: input text
    RETURNS:
        number of energized tiles
    """
    max_len = 0
    contraption = [[s for s in list(line)] for line in input_text.splitlines()]
    df = pd.DataFrame(contraption)
    for i in range(df.shape[1]):
        energized = set()
        start = (i, 0)
        direction = find_direction(df.iloc[start[1], start[0]], 'D')[0]
        navigate_iteratively(df, start, direction, energized)
        max_len = max(max_len, len(energized))
    for i in range(df.shape[1]):
        energized = set()
        start = (i, df.shape[0] - 1)
        direction = find_direction(df.iloc[start[1], start[0]], 'U')[0]
        navigate_iteratively(df, start, direction, energized)
        max_len = max(max_len, len(energized))
    for i in range(df.shape[0]):
        energized = set()
        start = (0, i)
        direction = find_direction(df.iloc[start[1], start[0]], 'R')[0]
        navigate_iteratively(df, start, direction, energized)
        max_len = max(max_len, len(energized))
    for i in range(df.shape[0]):
        energized = set()
        start = (df.shape[1] - 1, i)
        direction = find_direction(df.iloc[start[1], start[0]], 'L')[0]
        navigate_iteratively(df, start, direction, energized)
        max_len = max(max_len, len(energized))
    return max_len


sample = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

print(find_number_of_energized_tiles(sample))
with open('input.txt', 'r') as input_file:
    print(find_number_of_energized_tiles(input_file.read()))

print(find_number_of_energized_tiles_starting_from_each_border_point(sample))
with open('input.txt', 'r') as input_file:
    print(find_number_of_energized_tiles_starting_from_each_border_point(input_file.read()))
