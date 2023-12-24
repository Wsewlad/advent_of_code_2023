import pandas as pd


def grow(garden: pd.DataFrame, locations: set, step: int) -> set:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    new_locations = set()
    for location in locations:
        for direction in directions:
            new_location = (location[0] + direction[0], location[1] + direction[1])
            if (
                new_location[0] < 0
                or new_location[1] < 0
                or new_location[0] >= len(garden)
                or new_location[1] >= len(garden)
            ):
                continue
            if garden.iloc[new_location] != '#':
                garden.iloc[new_location] = str(step)
                new_locations.add(new_location)
    return new_locations


def find_number_of_garden_plots_at_step(input_text: str, steps: int) -> int:
    garden = [list(line) for line in input_text.splitlines()]
    garden = pd.DataFrame(garden)
    start = garden[garden == 'S'].stack().index[0]
    locations = {start}
    for step in range(steps):
        locations = grow(garden, locations, step + 1)
    return len(locations)





sample = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

print(find_number_of_garden_plots_at_step(sample, 6))
with open('input.txt', 'r') as f:
    print(find_number_of_garden_plots_at_step(f.read(), 64))
