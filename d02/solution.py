

def calculate_sum_of_game_ids(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        game, sets = line.split(":")
        game_id = game.strip().split(" ")[-1]
        cubes = sets.replace(";", ",").split(",")
        cube_rules = {"red": 12, "green": 13, "blue": 14}
        for rule in cube_rules:
            cube_numbres = sorted([int(cube.split()[0]) for cube in cubes if rule in cube])
            if cube_numbres[-1] > cube_rules[rule]:
                break
        else:
            result += int(game_id)
    return result


# with open('input.txt', "r") as file:
#     text = file.read()
#     sum_of_game_ids = calculate_sum_of_game_ids(text)
#     print(sum_of_game_ids)

sample = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

# sum_of_game_ids = calculate_sum_of_game_ids(sample)
# print(sum_of_game_ids)


def calculate_sum_of_power_of_minimum_sets_of_cubes(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        game, sets = line.split(":")
        cubes = sets.replace(";", ",").split(",")
        colors = ["red", "green", "blue"]
        power = 1
        for color in colors:
            cube_numbers_of_color = sorted([int(cube.split()[0]) for cube in cubes if color in cube])
            power *= cube_numbers_of_color[-1]
        result += power
    return result


sum_of_power = calculate_sum_of_power_of_minimum_sets_of_cubes(sample)
print(sum_of_power)

with open('input.txt', "r") as file:
    text = file.read()
    sum_of_power = calculate_sum_of_power_of_minimum_sets_of_cubes(text)
    print(sum_of_power)