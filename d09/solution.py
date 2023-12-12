

def find_extrapolated_value(values: list) -> int:
    extrapolated_values = [values]
    while set(extrapolated_values[-1]) != {0}:
        current_values = extrapolated_values[-1]
        extrapolated_values.append([current_values[i] - current_values[i - 1] for i in range(len(current_values))[1:]])
    extrapolated_values[-1].append(0)
    for i in reversed(range(len(extrapolated_values) - 1)):
        extrapolated_values[i].append(extrapolated_values[i + 1][-1] + extrapolated_values[i][-1])
    return extrapolated_values[0][-1]


def find_sum_of_extrapolated_values(input_text: str) -> int:
    result = sum([find_extrapolated_value([int(x) for x in line.split()]) for line in input_text.splitlines()])
    print(result)
    return result


sample = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

assert find_sum_of_extrapolated_values(sample) == 114

with open("input.txt", "r") as f:
    text = f.read()
    find_sum_of_extrapolated_values(text)
