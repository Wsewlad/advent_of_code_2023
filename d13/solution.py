import pandas as pd


def count_columns_reflections(df: pd.DataFrame, col_index: int) -> int:
    reflections = 0
    if col_index == -1:
        return reflections
    for i in range(col_index, -1, -1):
        j = col_index + col_index - i + 1
        if j >= len(df.columns):
            reflections = col_index + 1
            break
        # res = df[i] == df[j]
        # if res.where(res == False).count() == 1:
        #     df[i] = df[j]
        if not df[i].equals(df[j]):
            reflections = 0
            break
        reflections += 1
    return reflections


def count_rows_reflections(df: pd.DataFrame, row_index: int) -> int:
    reflections = 0
    if row_index == -1:
        return reflections
    # Count reflections
    for i in range(row_index, -1, -1):
        j = row_index + row_index - i + 1
        if j >= len(df.index):
            reflections = (row_index + 1) * 100
            break
        # res = df.iloc[i] == df.iloc[j]
        # if res.where(res == False).count() == 1:
        #     df.iloc[i] = df.iloc[j]
        if not df.iloc[i].equals(df.iloc[j]):
            reflections = 0
            break
        reflections += 100
    return reflections


def find_vertical_reflections(df: pd.DataFrame) -> int:
    lines_of_reflection = []
    for col in range(len(df.columns) - 1):
        if df[col].equals(df[col + 1]):
            lines_of_reflection.append(col)

        # res = df[col] == df[col + 1]
        # if res.where(res == False).count() == 1:
        #     df[col] = df[col + 1]
        #     lines_of_reflection.append(col)
    return max([count_columns_reflections(df, v_line) for v_line in lines_of_reflection], default=0)


def find_horizontal_reflections(df: pd.DataFrame) -> int:
    lines_of_reflection = []
    for row in range(len(df.index) - 1):
        if df.iloc[row].equals(df.iloc[row + 1]):
            lines_of_reflection.append(row)

        # res = df.iloc[row] == df.iloc[row + 1]
        # if res.where(res == False).count() == 1:
        #     df.iloc[row] = df.iloc[row + 1]
        #     lines_of_reflection.append(row)
    return max([count_rows_reflections(df, h_line) for h_line in lines_of_reflection], default=0)


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
# with open('input.txt', 'r') as f:
#     print(get_sum_of_reflections(f.read()))
