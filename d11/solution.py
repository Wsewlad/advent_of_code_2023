import pandas as pd


def get_manhattan_distance(p, q):
    """
    Return the manhattan distance between points p and q
    assuming both to have the same number of dimensions
    """
    distance = 0
    for p_i, q_i in zip(p, q):
        distance += abs(p_i - q_i)

    return distance


def prepare_df(input_text: str) -> (pd.DataFrame, list, list):
    """
    Return a dataframe with the input text and the empty rows and columns
    """
    df = pd.DataFrame([[*line] for line in input_text.splitlines()])
    empty_rows = df[df.eq(".").all(axis=1)].index.to_list()
    empty_columns = df[df.eq(".").all(axis=0)].index.to_list()
    return df, empty_rows, empty_columns


def find_sum_of_lengths_of_shortest_paths(input_text: str, expansion: int = 2) -> int:
    """
    Return the sum of the lengths of the shortest paths
    between each pair of points in the input text
    """
    df, empty_rows, empty_columns = prepare_df(input_text)
    points = [(y, int(x)) for y, x in df[df.eq("#")].stack().index.to_list()]
    distance = 0
    pairs = 0
    for i, p in enumerate(points):
        for q in points[i+1:]:
            # get number of empty rows and columns between p and q
            empty_rows_between = len(
                [r for r in empty_rows if (p[0] < r < q[0] if p[0] < q[0] else q[0] < r < p[0])]
            )
            empty_columns_between = len(
                [c for c in empty_columns if (p[1] < c < q[1] if p[1] < q[1] else q[1] < c < p[1])]
            )

            new_p = (p[0], p[1])
            new_q = (q[0], q[1])
            if new_p[0] > q[0]:
                new_p = (new_p[0] + (empty_rows_between * expansion) - empty_rows_between, new_p[1])
            else:
                new_q = (new_q[0] + (empty_rows_between * expansion) - empty_rows_between, new_q[1])
            if p[1] > q[1]:
                new_p = (new_p[0], new_p[1] + (empty_columns_between * expansion) - empty_columns_between)
            else:
                new_q = (new_q[0], new_q[1] + (empty_columns_between * expansion) - empty_columns_between)
            distance += get_manhattan_distance(new_p, new_q)
            pairs += 1
    print("pairs", pairs)
    return distance


sample = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

# part 1
print(find_sum_of_lengths_of_shortest_paths(sample))
with open("input.txt") as f:
    print(find_sum_of_lengths_of_shortest_paths(f.read()))

# part 2
print(find_sum_of_lengths_of_shortest_paths(sample, 100))
with open("input.txt") as f:
    print(find_sum_of_lengths_of_shortest_paths(f.read(), 1_000_000))
