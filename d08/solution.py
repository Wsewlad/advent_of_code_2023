import re


def find_amount_of_steps_to_reach_the_goal(input_text) -> int:
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    item = 'AAA'
    steps = 0
    while item != 'ZZZ':
        item = mapping[item][instructions[steps % len(instructions)]]
        steps += 1
    return steps


sample = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

sample2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

print(find_amount_of_steps_to_reach_the_goal(sample))
print(find_amount_of_steps_to_reach_the_goal(sample2))
with open('input.txt', 'r') as f:
    print(find_amount_of_steps_to_reach_the_goal(f.read()))

