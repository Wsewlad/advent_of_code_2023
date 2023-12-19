import math
from itertools import permutations


def count_arrangements(record: tuple) -> int:
    conditions, sizes = record
    parts = list(filter(None, conditions.split(".")))
    for i, p in enumerate(parts):
        if len(p) == sizes[i]:
            parts.pop(i)
            sizes.pop(i)
        else:
            break
    for i, p in enumerate(reversed(parts)):
        idx = -i - 1
        if len(p) == sizes[idx]:
            parts.pop(idx)
            sizes.pop(idx)
        else:
            break
    elements_in_parts = []
    for part in parts:
        elements = ""
        elements_count = 0
        while len(elements) < len(part):
            elements += ("".join(["#" for _ in range(sizes.pop(0))]))
            elements_count += 1
            if len(elements) < len(part):
                elements += "."
        elements_in_parts.append((elements, elements_count))
    perms = [(set(''.join(p) for p in permutations(part)), count) for part, count in elements_in_parts]
    valid_permutations = [len([v for v in p if len(list(filter(None, v.split(".")))) == count]) for p, count in perms]
    record_arrangements = sum(valid_permutations)
    print("Record: {} -> {}".format(record, record_arrangements))
    return record_arrangements


def find_sum_of_arrangements(input_text: str) -> int:
    records = [
        (conditions, [int(s) for s in sizes.split(",")])
        for conditions, sizes in [line.split() for line in input_text.splitlines()]
    ]
    return sum([count_arrangements(record) for record in records])


sample = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

print(find_sum_of_arrangements(sample))
