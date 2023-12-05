
def get_mapping(text_input: str) -> tuple:
    name, *rows = text_input.splitlines()
    name = name.split()[0]
    ranges = list()
    for row in rows:
        values = [int(n) for n in row.split()]
        ranges.append([values[1], values[0], values[-1]])
    return name, ranges


def parse_mappings(text_input: str) -> dict:
    name_to_ranges = dict()
    for line in text_input.split('\n\n')[1:]:
        name, ranges = get_mapping(line)
        name_to_ranges[name] = ranges
    return name_to_ranges


def map_value(value: int, ranges: dict) -> int:
    for source, destination, length in ranges:
        end = source + length
        if range(source, end).__contains__(value):
            return range(destination, destination + length)[value - source]
    return value


def find_the_lowest_location_number(text_input: str) -> int:
    lowest_location = 0
    seeds = [int(s) for s in text_input.split('seeds:')[1].split('\n')[0].split()]
    name_to_ranges = parse_mappings(text_input)
    for seed in seeds:
        soil = map_value(seed, name_to_ranges["seed-to-soil"])
        fertilizer = map_value(soil, name_to_ranges["soil-to-fertilizer"])
        water = map_value(fertilizer, name_to_ranges["fertilizer-to-water"])
        light = map_value(water, name_to_ranges["water-to-light"])
        temperature = map_value(light, name_to_ranges["light-to-temperature"])
        humidity = map_value(temperature, name_to_ranges["temperature-to-humidity"])
        location = map_value(humidity, name_to_ranges["humidity-to-location"])
        if location < lowest_location or lowest_location == 0:
            lowest_location = location
    return lowest_location


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

result = find_the_lowest_location_number(sample)
print(result)

with open('input.txt', "r") as file:
    text = file.read()
    result = find_the_lowest_location_number(text)
    print(result)
