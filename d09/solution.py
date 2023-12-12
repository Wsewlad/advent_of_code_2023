
def find_difference_distribution(values: list) -> list:
    """
    Find the difference distribution of a list of values.
    ARGS:
        values: list of values
    RETURNS:
        list of lists of values
    EXAMPLE:
        find_difference_distribution([1, 3, 6, 10, 15, 21]) -> [
            [1, 3, 6, 10, 15, 21], [2, 3, 4, 5, 6], [1, 1, 1, 1], [0, 0, 0]
        ]
    """
    difference_distribution = [values]
    while set(difference_distribution[-1]) != {0}:
        current_values = difference_distribution[-1]
        difference_distribution.append(
            [current_values[i] - current_values[i - 1] for i in range(len(current_values))[1:]]
        )
    return difference_distribution


def find_last_extrapolated_value(values: list) -> int:
    """
    Find the last extrapolated value of a list of values.
    ARGS:
        values: list of values
    RETURNS:
        int: last extrapolated value
    EXAMPLE:
        find_last_extrapolated_value([1, 3, 6, 10, 15, 21]) -> 28
    """
    extrapolated_values = find_difference_distribution(values)
    extrapolated_values[-1].append(0)
    for i in reversed(range(len(extrapolated_values) - 1)):
        extrapolated_values[i].append(extrapolated_values[i + 1][-1] + extrapolated_values[i][-1])
    return extrapolated_values[0][-1]


def find_first_extrapolated_value(values: list) -> int:
    """
    Find the first extrapolated value of a list of values.
    ARGS:
        values: list of values
    RETURNS:
        int: first extrapolated value
    EXAMPLE:
        find_first_extrapolated_value([1, 3, 6, 10, 15, 21]) -> 0
    """
    extrapolated_values = find_difference_distribution(values)
    extrapolated_values[-1].insert(0, 0)
    for i in reversed(range(len(extrapolated_values) - 1)):
        extrapolated_values[i].insert(0, extrapolated_values[i][0] - extrapolated_values[i + 1][0])
    return extrapolated_values[0][0]


def find_sum_of_extrapolated_values_part_1(input_text: str) -> int:
    result = sum([find_last_extrapolated_value([int(x) for x in line.split()]) for line in input_text.splitlines()])
    print(result)
    return result


def find_sum_of_extrapolated_values_part_2(input_text: str) -> int:
    result = sum([find_first_extrapolated_value([int(x) for x in line.split()]) for line in input_text.splitlines()])
    print(result)
    return result


sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

# assert find_sum_of_extrapolated_values_part_1(sample) == 114
# with open("input.txt", "r") as f:
#     text = f.read()
#     find_sum_of_extrapolated_values_part_1(text)


assert find_sum_of_extrapolated_values_part_2(sample) == 2
with open("input.txt", "r") as f:
    text = f.read()
    find_sum_of_extrapolated_values_part_2(text)