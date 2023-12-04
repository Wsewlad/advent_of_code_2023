import re


def calculate_sum_of_all_of_the_calibration_values(input_text: str) -> int:
    """
    Splits the input text into lines.
    For each line, finds all digits and concatenates the first and the last one.
    Then summs all the values.
    ARGS:
        input_text: str
    RETURNS:
        result: int
    """
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        digits = re.findall(r'\d', line)
        if any(digits):
            calibration_value = digits[0] + digits[-1]
            result += int(calibration_value)
    return result


def calculate_sum_of_all_of_the_calibration_values_part_2(input_text: str) -> int:
    """
    Splits the input text into lines. For each line, iterates over all the characters and finds all the digits.
    Then concatenates the first and the last digit and sums all the values.
    ARGS:
        input_text: str
    RETURNS:
        result: int
    """
    pattern = r'\d|one|two|three|four|five|six|seven|eight|nine'
    digit_map = {
        '1': '1', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '8': '8', '9': '9',
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
        'nine': '9'
    }
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        start = 0
        digits = []
        while start < len(line):
            digits += re.findall(pattern, line[start:])
            start += 1
        if any(digits):
            calibration_value = digit_map[digits[0]] + digit_map[digits[-1]]
            result += int(calibration_value)
    return result


# with open('input.txt', "r") as file:
#     text = file.read()
#     calibration_values_sum = calculate_sum_of_all_of_the_calibration_values(text)
#     print(calibration_values_sum)

# example = """
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# """
# calibration_values_sum = calculate_sum_of_all_of_the_calibration_values(example)
# print(calibration_values_sum)

with open('input.txt', "r") as file:
    text = file.read()
    calibration_values_sum = calculate_sum_of_all_of_the_calibration_values_part_2(text)
    print(calibration_values_sum)

example_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""
calibration_values_sum = calculate_sum_of_all_of_the_calibration_values_part_2(example_2)
print(calibration_values_sum)

example_3 = """
gsjgklneight6zqfz
7one718onegfqtdbtxfcmd
xvtfhkm8c9
914two8
"""
calibration_values_sum = calculate_sum_of_all_of_the_calibration_values_part_2(example_3)
print(calibration_values_sum)