import re
import itertools
import math


def find_amount_of_steps_to_reach_the_goal_part_1(input_text) -> int:
    """
    Splits input text into lines, then parses instructions and mapping.
    Then it iterates over instructions and mapping until it reaches the goal.
    """
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    item = 'AAA'
    steps = 0
    while item != 'ZZZ':
        item = mapping[item][instructions[steps % len(instructions)]]
        steps += 1
    return steps


def find_amount_of_steps_to_reach_the_goal_part_2(input_text) -> int:
    """
    Splits input text into lines, then parses instructions and mapping.
    Then it iterates over instructions and mapping until it reaches the goal.
    """
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    nodes = [key for key, _ in mapping.items() if key.endswith('A')]

    def mapper(node):
        for op in itertools.cycle(instructions):
            yield node
            node = mapping[node][op]

    def steps(mapped_nodes):
        step = 0
        for node in mapped_nodes:
            if node.endswith('Z'):
                return step
            step += 1
    mapped = [steps(mapper(node)) for node in nodes]
    same_step = math.lcm(*mapped)
    return same_step



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

# print(find_amount_of_steps_to_reach_the_goal_part_1(sample))
# # print(find_amount_of_steps_to_reach_the_goal_part_1(sample2))
# with open('input.txt', 'r') as f:
#     print(find_amount_of_steps_to_reach_the_goal_part_1(f.read()))

sample3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

print(find_amount_of_steps_to_reach_the_goal_part_2(sample3))
with open('input.txt', 'r') as f:
    print(find_amount_of_steps_to_reach_the_goal_part_2(f.read()))
