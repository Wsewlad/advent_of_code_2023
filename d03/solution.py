import re
import pandas as pd
import math


def is_number_valid(span: tuple, lines: list) -> bool:
    start = 0 if span[0] - 1 < 0 else span[0] - 1
    end = len(lines[1]) if span[1] + 1 > len(lines[1]) else span[1] + 1
    for line in lines:
        if re.search(r'[^\.\d]', line[start:end]):
            return True
    return False


def get_sum_of_all_part_numbers(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for idx, line in enumerate(lines):
        lines_to_check = [
            lines[idx - 1] if idx != 0 else "",
            line,
            lines[idx + 1] if idx != len(lines) - 1 else ""
        ]
        numbers = re.findall(r'\d+', line)
        for number in numbers:
            span = re.search(fr"\b{number}\b", line).span()
            if is_number_valid(span, lines_to_check):
                result += int(number)
    return result


def find_gear_ratios(span: tuple, lines: list) -> int:
    start = 0 if span[0] - 1 < 0 else span[0] - 1
    end = len(lines[1]) if span[1] + 1 > len(lines[1]) else span[1] + 1
    star_interval = pd.Interval(start, end)
    results = []
    for line in lines:
        results += [
            int(m.group(0)) for m in re.finditer(r'\d+', line)
            if pd.Interval(m.start(), m.end()).overlaps(star_interval)
        ]
    if len(results) > 1:
        return math.prod(results)
    return 0


def get_sum_of_all_gear_ratios(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for idx, line in enumerate(lines):
        lines_to_check = [
            lines[idx - 1] if idx != 0 else "",
            line,
            lines[idx + 1] if idx != len(lines) - 1 else ""
        ]
        start_spans = [m.span() for m in re.finditer(r'\*', line)]
        for span in start_spans:
            result += find_gear_ratios(span, lines_to_check)
    return result


# with open('input.txt', "r") as file:
#     text = file.read()
#     sum_of_numbers = get_sum_of_all_part_numbers(text)
#     print(sum_of_numbers)

sample = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# sum_of_numbers = get_sum_of_all_part_numbers(sample)
# print(sum_of_numbers)

with open('input.txt', "r") as file:
    text = file.read()
    sum_of_all_gear_ratios = get_sum_of_all_gear_ratios(text)
    print(sum_of_all_gear_ratios)

sum_of_all_gear_ratios = get_sum_of_all_gear_ratios(sample)
print(sum_of_all_gear_ratios)
