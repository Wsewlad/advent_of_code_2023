import numpy as np


def find_number_of_ways_to_beat_the_record(races: list) -> int:
    return np.prod(
        [
            len(
                [m for m in range(race[0] - 1) if m * (race[0] - m) > race[1]]
            )
            for race in races
        ]
    )


sample = """Time:      7  15   30
Distance:  9  40  200
"""


def part_1(input_text: str) -> int:
    lines = [map(lambda x: int(x), line.split(":")[1].split()) for line in input_text.splitlines()]
    races = list(zip(*lines))
    return find_number_of_ways_to_beat_the_record(races)


def part_2(input_text: str) -> int:
    race = [int(line.split(":")[1].replace(" ", "")) for line in input_text.splitlines()]
    return find_number_of_ways_to_beat_the_record([(race[0], race[1])])


# print(part_1(sample))
# with open("input.txt", "r") as f:
#     print(part_1(f.read()))

print(part_2(sample))
with open("input.txt", "r") as f:
    print(part_2(f.read()))
