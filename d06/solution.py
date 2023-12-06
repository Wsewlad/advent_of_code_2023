import numpy as np


def find_number_of_ways_to_beat_the_record(input: str) -> int:
    lines = [map(lambda x: int(x), line.split(":")[1].split()) for line in input.splitlines()]
    races = list(zip(*lines))
    ways_to_beat_the_record = [
        len(
            [m for m in range(race[0] - 1) if m * (race[0] - m) > race[1]]
        )
        for race in races
    ]
    return np.prod(ways_to_beat_the_record)


sample = """Time:      7  15   30
Distance:  9  40  200
"""

print(
    find_number_of_ways_to_beat_the_record(sample)
)

with open("input.txt", "r") as f:
    print(
        find_number_of_ways_to_beat_the_record(f.read())
    )
