import pandas as pd


def find_the_total_load(input_text: str) -> int:
    df = pd.DataFrame([list(row) for row in input_text.splitlines()])
    # Shift all 'O' to the top
    for i in range(1, len(df)):
        for j in range(len(df.columns)):
            if df.iloc[i, j] == 'O':
                current_row_idx = i
                while df.iloc[current_row_idx - 1, j] == '.' and current_row_idx > 0:
                    df.iloc[current_row_idx - 1, j] = 'O'
                    df.iloc[current_row_idx, j] = '.'
                    current_row_idx -= 1
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

print(find_the_total_load(sample))
with open('input.txt', 'r') as f:
    print(find_the_total_load(f.read()))
