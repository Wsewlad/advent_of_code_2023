import time


def get_mapping(text_input: str) -> tuple:
    """
    Parses the mappings from the text input
    ARGS:
        text_input (str): The text input
    RETURNS:
        tuple: The name of the mapping and the mapping itself
    """
    name, *rows = text_input.splitlines()
    name = name.split()[0]
    ranges = list()
    for row in rows:
        values = [int(n) for n in row.split()]
        ranges.append([values[1], values[0], values[-1]])
    return name, sorted(ranges, key=lambda x: x[0])


def parse_mappings(text_input: str) -> dict:
    """
    Parses the mappings from the text input
    ARGS:
        text_input (str): The text input
    RETURNS:
        dict: A dictionary of the mappings
    """
    name_to_ranges = dict()
    for line in text_input.split('\n\n')[1:]:
        name, ranges = get_mapping(line)
        name_to_ranges[name] = ranges
    return name_to_ranges


def map_value(value: int, ranges: list) -> int:
    """
    Maps a value to a new value based on the ranges
    ARGS:
        value (int): The value to map
        ranges (list): The ranges to map the value to
    RETURNS:
        int: The mapped value
    """
    if ranges[0][0] <= value < ranges[-1][0] + ranges[-1][2]:
        for source, destination, length in ranges:
            if source <= value < source + length:
                return destination + value - source
    else:
        return value


def reverse_map_value(value: int, ranges: list) -> int:
    """
    Maps a value to a new value based on the ranges
    ARGS:
        value (int): The value to map
        ranges (list): The ranges to map the value to
    RETURNS:
        int: The mapped value
    """
    ranges = sorted(ranges, key=lambda x: x[1])
    if ranges[0][1] <= value < ranges[-1][1] + ranges[-1][2]:
        for source, destination, length in ranges:
            if destination <= value < destination + length:
                return source + value - destination
    else:
        return value


def seed_to_location(seed: int, mapping: dict) -> int:
    """
    Maps a seed to a location
    ARGS:
        seed (int): The seed
        mapping (dict): The mapping
    RETURNS:
        int: The location
    """
    soil = map_value(seed, mapping["seed-to-soil"])
    fertilizer = map_value(soil, mapping["soil-to-fertilizer"])
    water = map_value(fertilizer, mapping["fertilizer-to-water"])
    light = map_value(water, mapping["water-to-light"])
    temperature = map_value(light, mapping["light-to-temperature"])
    humidity = map_value(temperature, mapping["temperature-to-humidity"])
    location = map_value(humidity, mapping["humidity-to-location"])
    return location


def location_to_seed(location: int, mapping: dict) -> int:
    """
    Maps a location to a seed
    ARGS:
        location (int): The location
        mapping (dict): The mapping
    RETURNS:
        int: The seed
    """
    humidity = reverse_map_value(location, mapping["humidity-to-location"])
    temperature = reverse_map_value(humidity, mapping["temperature-to-humidity"])
    light = reverse_map_value(temperature, mapping["light-to-temperature"])
    water = reverse_map_value(light, mapping["water-to-light"])
    fertilizer = reverse_map_value(water, mapping["fertilizer-to-water"])
    soil = reverse_map_value(fertilizer, mapping["soil-to-fertilizer"])
    seed = reverse_map_value(soil, mapping["seed-to-soil"])
    return seed


def part1(text_input: str) -> int:
    """
    Calculates the lowest location of the seeds
    ARGS:
        text_input (str): The text input
    RETURNS:
        int: The lowest location
    """
    seeds = [int(s) for s in text_input.split('seeds:')[1].split('\n')[0].split()]
    mapping = parse_mappings(text_input)
    lowest_location = 0
    for seed in seeds:
        location = seed_to_location(seed, mapping)
        if location < lowest_location or lowest_location == 0:
            lowest_location = location
    return lowest_location


def part2(text_input: str) -> int:
    """
    Calculates the location of the seeds that are in the same range as the seeds in the text input
    ARGS:
        text_input (str): The text input
    RETURNS:
        int: The lowest location
    """
    seeds = [int(s) for s in text_input.split('seeds:')[1].split('\n')[0].split()]
    mapping = parse_mappings(text_input)
    seed_ranges = [range(seed, seed + seeds[idx + 1]) for idx, seed in enumerate(seeds) if (idx + 1) % 2 != 0]
    location_ranges = sorted(mapping["humidity-to-location"], key=lambda x: x[1])
    for location in range(0, location_ranges[-1][1] + location_ranges[-1][2]):
        seed = location_to_seed(location, mapping)
        if any([r for r in seed_ranges if seed in r]):
            return location


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

# result = part1(sample)
# print(result)
# #
# with open('input.txt', "r") as file:
#     text = file.read()
#     result = part1(text)
#     print(result)

result = part2(sample)
print(result)

with open('input.txt', "r") as file:
    text = file.read()
    start_time = time.time()
    result = part2(text)
    print(result)
    print("Time: %02d:%02d" % (divmod(time.time() - start_time, 60)))

