import pandas as pd


def count_columns_reflections(df: pd.DataFrame, col_index: int, part2: bool = False) -> int:
    """
    Counts reflections in columns from the given index to the left side of the dataframe.
    ARGS:
        df: dataframe
        col_index: index of column to start counting reflections from
        part2: if True, also counts reflections with one different value
    RETURNS:
        number of reflections
    """
    reflections = 0
    for i in range(col_index, -1, -1):
        j = col_index + col_index - i + 1
        if j >= len(df.columns):
            reflections = col_index + 1
            break
        res = df[i] == df[j]
        if not df[i].equals(df[j]):
            if part2 and res.where(res == False).count() == 1:
                pass
            else:
                reflections = 0
                break
        reflections += 1
    return reflections


def count_rows_reflections(df: pd.DataFrame, row_index: int, part2: bool = False) -> int:
    """
    Counts reflections in rows from the given index to the top of the dataframe.
    ARGS:
        df: dataframe
        row_index: index of row to start counting reflections from
        part2: if True, also counts reflections with one different value
    RETURNS:
        number of reflections
    """
    reflections = 0
    for i in range(row_index, -1, -1):
        j = row_index + row_index - i + 1
        if j >= len(df.index):
            reflections = (row_index + 1) * 100
            break
        res = df.iloc[i] == df.iloc[j]
        if not df.iloc[i].equals(df.iloc[j]):
            if part2 and res.where(res == False).count() == 1:
                pass
            else:
                reflections = 0
                break
        reflections += 100
    return reflections


# Part 1
def find_vertical_reflections_part1(df: pd.DataFrame) -> int:
    """
    Finds vertical reflections in the given dataframe.
    ARGS:
        df: dataframe
    RETURNS:
        number of reflections
    """
    lines_of_reflection = {col for col in range(len(df.columns) - 1) if df[col].equals(df[col + 1])}
    return max([count_columns_reflections(df, v_line) for v_line in lines_of_reflection], default=0)


def find_horizontal_reflections_part1(df: pd.DataFrame) -> int:
    """
    Finds horizontal reflections in the given dataframe.
    ARGS:
        df: dataframe
    RETURNS:
        number of reflections
    """
    lines_of_reflection = {row for row in range(len(df.index) - 1) if df.iloc[row].equals(df.iloc[row + 1])}
    return max([count_rows_reflections(df, h_line) for h_line in lines_of_reflection], default=0)


def get_sum_of_reflections_part1(input_text: str) -> int:
    """
    Gets sum of reflections in the given input text.
    ARGS:
        input_text: input text
    RETURNS:
        number of reflections
    """
    reflections = 0
    patterns = input_text.split('\n\n')
    for pattern in patterns:
        df = pd.DataFrame([list(row) for row in pattern.splitlines()])
        reflections += find_vertical_reflections_part1(df)
        reflections += find_horizontal_reflections_part1(df)
    return reflections


# Part 2
def find_vertical_reflections_part2(df: pd.DataFrame) -> int:
    """
    Finds different from part1 vertical reflections in the given dataframe.
    It also counts reflections with one different value.
    ARGS:
        df: dataframe
    RETURNS:
        number of reflections
    """
    lines_of_reflection1 = set()
    lines_of_reflection2 = set()
    for col in range(len(df.columns) - 1):
        if df[col].equals(df[col + 1]):
            lines_of_reflection1.add(col)

        res = df[col] == df[col + 1]
        if res.where(res == False).count() == 1:
            lines_of_reflection2.add(col)
    lines_of_reflection = lines_of_reflection2.union(lines_of_reflection1)
    reflections1 = [(line, count_columns_reflections(df, line)) for line in lines_of_reflection1]
    reflections2 = [(line, count_columns_reflections(df, line, True)) for line in lines_of_reflection]
    reflections = [r for r in reflections2 if r not in reflections1]
    return max([r for _, r in reflections], default=0)


def find_horizontal_reflections_part2(df: pd.DataFrame) -> int:
    """
    Finds different from part1 horizontal reflections in the given dataframe.
    It also counts reflections with one different value.
    ARGS:
        df: dataframe
    RETURNS:
        number of reflections
    """
    lines_of_reflection1 = set()
    lines_of_reflection2 = set()
    for row in range(len(df.index) - 1):
        if df.iloc[row].equals(df.iloc[row + 1]):
            lines_of_reflection1.add(row)

        res = df.iloc[row] == df.iloc[row + 1]
        if res.where(res == False).count() == 1:
            lines_of_reflection2.add(row)
    lines_of_reflection = lines_of_reflection2.union(lines_of_reflection1)
    reflections1 = [(line, count_rows_reflections(df, line)) for line in lines_of_reflection1]
    reflections2 = [(line, count_rows_reflections(df, line, True)) for line in lines_of_reflection]
    reflections = [r for r in reflections2 if r not in reflections1]
    return max([r for _, r in reflections], default=0)


def get_sum_of_reflections_part2(input_text: str) -> int:
    """
    Gets sum of different from part1 reflections in the given input text.
    ARGS:
        input_text: input text
    RETURNS:
        number of reflections
    """
    reflections = 0
    patterns = input_text.split('\n\n')
    for pattern in patterns:
        df = pd.DataFrame([list(row) for row in pattern.splitlines()])
        reflections += find_vertical_reflections_part2(df)
        reflections += find_horizontal_reflections_part2(df)
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

print(get_sum_of_reflections_part1(sample))
with open('input.txt', 'r') as f:
    print(get_sum_of_reflections_part1(f.read()))

print(get_sum_of_reflections_part2(sample))
with open('input.txt', 'r') as f:
    print(get_sum_of_reflections_part2(f.read()))
    # 31836
