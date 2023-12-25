import pandas as pd


def shift_to_north(df: pd.DataFrame) -> None:
    """
    Shifts all 'O' to the north.
    Args:
        df: dataframe
    Returns:
        None
    """
    spans = df[df == 'O'].stack().index.tolist()
    for span in spans:
        if span[0] > 0:
            prev_cells = df.iloc[:span[0], span[1]]
            nearest_not_empty_cell = ([-1] + prev_cells[prev_cells != '.'].index.tolist())[-1]
            if nearest_not_empty_cell + 1 != span[0]:
                df.iloc[nearest_not_empty_cell + 1, span[1]] = 'O'
                df.iloc[span[0], span[1]] = '.'


def shift_to_west(df: pd.DataFrame) -> None:
    """
    Shifts all 'O' to the west.
    Args:
        df: dataframe
    Returns:
        None
    """
    spans = df[df == 'O'].stack().index.tolist()
    for span in spans:
        if span[1] > 0:
            prev_cells = df.iloc[span[0], :span[1]]
            nearest_not_empty_cell = ([-1] + prev_cells[prev_cells != '.'].index.tolist())[-1]
            if nearest_not_empty_cell + 1 != span[1]:
                df.iloc[span[0], nearest_not_empty_cell + 1] = 'O'
                df.iloc[span[0], span[1]] = '.'


def shift_to_south(df: pd.DataFrame) -> None:
    """
    Shifts all 'O' to the south.
    Args:
        df: dataframe
    Returns:
        None
    """
    spans = df[df == 'O'].stack().index.tolist()
    for span in spans[::-1]:
        if span[0] < len(df) - 1:
            prev_cells = df.iloc[span[0] + 1:, span[1]]
            farthest_not_empty_cell = (prev_cells[prev_cells != '.'].index.tolist() + [len(df)])[0]
            if farthest_not_empty_cell - 1 != span[0]:
                df.iloc[farthest_not_empty_cell - 1, span[1]] = 'O'
                df.iloc[span[0], span[1]] = '.'


def shift_to_east(df: pd.DataFrame) -> None:
    """
    Shifts all 'O' to the east.
    Args:
        df: dataframe
    Returns:
        None
    """
    spans = df[df == 'O'].stack().index.tolist()
    for span in spans[::-1]:
        if span[1] < len(df.columns) - 1:
            prev_cells = df.iloc[span[0], span[1] + 1:]
            farthest_not_empty_cell = (prev_cells[prev_cells != '.'].index.tolist() + [len(df.columns)])[0]
            if farthest_not_empty_cell - 1 != span[1]:
                df.iloc[span[0], farthest_not_empty_cell - 1] = 'O'
                df.iloc[span[0], span[1]] = '.'


# 98029
def find_the_total_load(input_text: str, part2: bool = False) -> int:
    df = pd.DataFrame([list(row) for row in input_text.splitlines()])
    if part2:
        steps = 1000000000
        seen = dict()
        for step in range(steps):
            spans = str(df[df == 'O'].stack().index.tolist())
            if (prev_step := seen.get(spans)) is not None:
                next_since_prev = step - prev_step
                last_step = step
                break
            seen[spans] = step
            shift_to_north(df)
            shift_to_west(df)
            shift_to_south(df)
            shift_to_east(df)
        for _ in range((steps - last_step) % next_since_prev):
            shift_to_north(df)
            shift_to_west(df)
            shift_to_south(df)
            shift_to_east(df)
    else:
        shift_to_north(df)
    total_load = 0
    for i in range(len(df)):
        total_load += df.iloc[i].tolist().count('O') * (len(df) - i)
    return total_load


sample = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

print(find_the_total_load(sample, part2=True))
with open('input.txt', 'r') as f:
    print(find_the_total_load(f.read(), part2=True))
