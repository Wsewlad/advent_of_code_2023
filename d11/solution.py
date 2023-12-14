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


def prepare_df(input_text: str) -> pd.DataFrame:
    """
    Return a dataframe with the input text
    """
    df = pd.DataFrame([[*line] for line in input_text.splitlines()])

    # add duplicate rows if needed
    for y in df.index:
        if "#" in df.loc[y].values:
            continue
        else:
            df.loc[y - 0.5] = "."
    df = df.sort_index().reset_index(drop=True)

    # add duplicate columns if needed
    inserted = 0
    for x in df.columns:
        if "#" in df[x].values:
            continue
        else:
            df.insert(int(x) + inserted, str(x) + "_copy", ".")
            inserted += 1
    df = df.set_axis([str(i) for i in range(len(df.columns))], axis=1)
    return df


def find_sum_of_lengths_of_shortest_paths(input_text: str) -> int:
    """
    Return the sum of the lengths of the shortest paths
    between each pair of points in the input text
    """
    df = prepare_df(input_text)
    points = [(y, int(x)) for y, x in df[df.eq("#")].stack().index.to_list()]
    distance = 0
    pairs = 0
    for i, p in enumerate(points):
        for q in points[i+1:]:
            distance += get_manhattan_distance(p, q)
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

print(find_sum_of_lengths_of_shortest_paths(sample))
with open("input.txt") as f:
    print(find_sum_of_lengths_of_shortest_paths(f.read()))