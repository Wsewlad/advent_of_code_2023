import pandas as pd


def find_vertical_reflections(df: pd.DataFrame) -> int:
    reflections = 0
    col_index = -1
    # Find first column that is equal to the next one
    for col in range(len(df.columns) - 1):
        if df[col].equals(df[col + 1]):
            col_index = col
            break
    # Count reflections
    if col_index == -1:
        return reflections
    for i in range(col_index, -1, -1):
        j = col_index + col_index - i + 1
        if j >= len(df.columns):
            reflections = col_index + 1
            break
        if not df[i].equals(df[j]):
            reflections = 0
            break
    return reflections


def find_horizontal_reflections(df: pd.DataFrame) -> int:
    reflections = 0
    row_index = -1
    # Find first row that is equal to the next one
    for row in range(len(df.index) - 1):
        if df.iloc[row].equals(df.iloc[row + 1]):
            row_index = row
            break
    if row_index == -1:
        return reflections
    # Count reflections
    for i in range(row_index, -1, -1):
        j = row_index + row_index - i + 1
        if j >= len(df.index):
            reflections = (row_index + 1) * 100
            break
        if not df.iloc[i].equals(df.iloc[j]):
            reflections = 0
            break
    return reflections


def get_sum_of_reflections(input_text: str) -> int:
    reflections = 0
    patterns = input_text.split('\n\n')
    for pattern in patterns:
        # Parse input into pandas dataframe
        df = pd.DataFrame([list(row) for row in pattern.splitlines()])
        reflections += find_vertical_reflections(df)
        reflections += find_horizontal_reflections(df)

    return reflections


sample = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""

print(get_sum_of_reflections(sample))
with open('input.txt', 'r') as f:
    print(get_sum_of_reflections(f.read()))
