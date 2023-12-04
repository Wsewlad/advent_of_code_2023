import functools


# Part 1
def get_intersections(line: str) -> set:
    winning_numbers, numbers = line.split(':')[1].split('|')
    winning_numbers = set([int(x) for x in winning_numbers.split()])
    numbers = set([int(x) for x in numbers.split()])
    return winning_numbers.intersection(numbers)


def get_cards_total_points(input_text: str) -> int:
    result = 0
    lines = input_text.splitlines()
    for line in lines:
        intersections = get_intersections(line)
        if any(intersections):
            result += functools.reduce(lambda x, y: x * 2, range(1, len(intersections)), 1)
    return result


# with open('input.txt', "r") as file:
#     text = file.read()
#     total_points = get_cards_total_points(text)
#     print(total_points)


sample = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# total_points = get_cards_total_points(sample)
# print(total_points)


# Part 2
def get_scratchcards_total(input_text: str) -> int:
    lines = input_text.splitlines()
    lines_len = len(lines)
    copies = [0]*lines_len
    for idx, line in enumerate(lines):
        copies[idx] += 1
        intersections = get_intersections(line)
        if any(intersections):
            for i in range(1, len(intersections) + 1):
                card_index_to_add_copies = (idx + i) % (lines_len - 1)
                copies[card_index_to_add_copies] += 1 * copies[idx]
        elif copies[idx] == 0:
            copies[idx] = 1
            break
    return sum(copies)


with open('input.txt', "r") as file:
    text = file.read()
    total_scratchcards = get_scratchcards_total(text)
    print(total_scratchcards)

total_scratchcards = get_scratchcards_total(sample)
print(total_scratchcards)
