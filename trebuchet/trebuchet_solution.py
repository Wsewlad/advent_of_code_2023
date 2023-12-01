import re


def calculate_sum_of_all_of_the_calibration_values(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        digits = re.findall(r'\d', line)
        if any(digits):
            calibration_value = digits[0] + digits[-1]
            result += int(calibration_value)
    return result


with open('input.txt', "r") as file:
    text = file.read()
    calibration_values_sum = calculate_sum_of_all_of_the_calibration_values(text)
    print(calibration_values_sum)


example = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""
calibration_values_sum = calculate_sum_of_all_of_the_calibration_values(example)
print(calibration_values_sum)
