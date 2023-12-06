from itertools import chain


def get_mapping(text_input: str) -> tuple:
    name, *rows = text_input.splitlines()
    name = name.split()[0]
    ranges = list()
    for row in rows:
        values = [int(n) for n in row.split()]
        ranges.append([values[1], values[0], values[-1]])
    return name, sorted(ranges, key=lambda x: x[0])


def parse_mappings(text_input: str) -> dict:
    name_to_ranges = dict()
    for line in text_input.split('\n\n')[1:]:
        name, ranges = get_mapping(line)
        name_to_ranges[name] = ranges
    return name_to_ranges


def map_value(value: int, ranges: list) -> int:
    try:
        if ranges[0][0] <= value < ranges[-1][0] + ranges[-1][2]:
            for source, destination, length in ranges:
                if source <= value < source + length:
                    return destination + value - source
        else:
            return value
    except:
        return value


def seed_to_location(seed: int, mapping: dict) -> int:
    soil = map_value(seed, mapping["seed-to-soil"])
    fertilizer = map_value(soil, mapping["soil-to-fertilizer"])
    water = map_value(fertilizer, mapping["fertilizer-to-water"])
    light = map_value(water, mapping["water-to-light"])
    temperature = map_value(light, mapping["light-to-temperature"])
    humidity = map_value(temperature, mapping["temperature-to-humidity"])
    location = map_value(humidity, mapping["humidity-to-location"])
    return location


def part1(text_input: str) -> int:
    seeds = [int(s) for s in text_input.split('seeds:')[1].split('\n')[0].split()]
    mapping = parse_mappings(text_input)
    lowest_location = 0
    for seed in seeds:
        location = seed_to_location(seed, mapping)
        if location < lowest_location or lowest_location == 0:
            lowest_location = location
    return lowest_location


def part2(text_input: str) -> int:
    seeds = [int(s) for s in text_input.split('seeds:')[1].split('\n')[0].split()]
    mapping = parse_mappings(text_input)
    seed_to_range = {seed: seeds[idx + 1] for idx, seed in enumerate(seeds) if (idx + 1) % 2 != 0}
    seeds = [
        range(initial_seed, initial_seed + length) for initial_seed, length in seed_to_range.items()
    ]
    # seeds = [
    #     (initial_seed + idx for idx, x in enumerate(range(length))) for initial_seed, length in seed_to_range.items()
    # ]
    seeds = chain.from_iterable(seeds)
    return min(
        (seed_to_location(x, mapping) for x in seeds)
    )
    # return min(
    #     (
    #         min((seed_to_location(x, mapping) for x in s)) for s
    #         in seeds
    #     )
    # )


sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""

result = part1(sample)
print(result)
# #
# with open('input.txt', "r") as file:
#     text = file.read()
#     result = part1(text)
#     print(result)

result = part2(sample)
print(result)

with open('input.txt', "r") as file:
    text = file.read()
    result = part2(text)
    print(result)
