import re


def is_number_valid(span: tuple, lines: list) -> bool:
    symbols_patter = r'[^\.\d]'
    start = 0 if span[0] - 1 < 0 else span[0] - 1
    end = len(lines[1]) if span[1] + 1 > len(lines[1]) else span[1] + 1
    for line in lines:
        if re.search(symbols_patter, line[start:end]):
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


with open('input.txt', "r") as file:
    text = file.read()
    sum_of_numbers = get_sum_of_all_part_numbers(text)
    print(sum_of_numbers)

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

sum_of_numbers = get_sum_of_all_part_numbers(sample)
print(sum_of_numbers)
