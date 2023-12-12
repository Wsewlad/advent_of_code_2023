import re
import time
# import asyncio
from multiprocessing import Process, Pipe, freeze_support, Pool, Queue, Lock, Array, Manager


def find_amount_of_steps_to_reach_the_goal_part_1(input_text) -> int:
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    item = 'AAA'
    steps = 0
    while item != 'ZZZ':
        item = mapping[item][instructions[steps % len(instructions)]]
        steps += 1
    return steps


def find_amount_of_steps_to_reach_the_goal_part_3(input_text) -> int:
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    nodes = [key for key, _ in mapping.items() if key.endswith('A')]
    # nodes = nodes[:4]
    print(nodes)
    # steps = 0
    for i in range(100_000_000_000):
        nodes = [
            mapping[nodes[0]][instructions[i % len(instructions)]],
            mapping[nodes[1]][instructions[i % len(instructions)]],
            mapping[nodes[2]][instructions[i % len(instructions)]],
            mapping[nodes[3]][instructions[i % len(instructions)]],
            mapping[nodes[4]][instructions[i % len(instructions)]],
            mapping[nodes[5]][instructions[i % len(instructions)]],
        ]
        # steps += 1
        if all([
            nodes[0].endswith('Z'),
            nodes[1].endswith('Z'),
            nodes[2].endswith('Z'),
            nodes[3].endswith('Z'),
            nodes[4].endswith('Z'),
            nodes[5].endswith('Z'),
        ]):
            return i + 1
        # if len([n for n in nodes if n.endswith('Z')]) == len(nodes):
        #     return i + 1
    return 0


async def find_amount_of_steps_to_reach_the_goal_part_2(input_text):
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    # reversed_instructions = list(reversed(instructions))
    instructions_len = len(instructions)
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    nodes = [key for key, _ in mapping.items() if key.endswith('A')]
    nodes = nodes[:4]
    print(nodes)
    nodes_len = len(nodes)
    steps = [({0}, nodes[i]) for i in range(nodes_len)]
    all_steps = [set() for _ in range(nodes_len)]
    unique_steps = set()
    # while len([n for n in nodes if n.endswith('Z')]) != nodes_len:
    #     nodes = [mapping[node][instructions[steps % len(instructions)]] for node in nodes]
    #     steps += 1
    range_len = mapping.__len__() * 5000
    result = 0
    # Time: 00:47
    while result == 0:
        steps = await asyncio.gather(*[async_find_amount_of_steps_to_reach_the_goal(steps[i][1], mapping, instructions, max(steps[i][0]), range_len) for i, n in enumerate(nodes)])
        # [all_steps[i].update(step[0]) for i, step in enumerate(steps)]
        all_steps = [step[0] for i, step in enumerate(steps)]
        intersection = all_steps[0].intersection(*all_steps)
        result = min(intersection) if intersection else 0
        # unique_steps = set([step[0] for step in steps])
    return result

    # 367 000 000
    # return check_all_nodes_in_the_loop_recursively(mapping, nodes, instructions, steps, range_len, nodes_len, instructions_len)
    # return [check_all_nodes_in_the_loop_recursively(mapping, [node], instructions, steps, range_len, 1, instructions_len) for node in nodes]
    # for i in range(range_len):
    #     nodes = [mapping[node][instructions[steps % len(instructions)]] for node in nodes]
    #     steps += 1
    #     if len([n for n in nodes if n.endswith('Z')]) == nodes_len:
    #         break
    # return steps


# async def async_find_amount_of_steps_to_reach_the_goal(node, mapping, instructions, steps, range_len):
#     return await asyncio.to_thread(sync_find_amount_of_steps_to_reach_the_goal, node, mapping, instructions, steps, range_len)


def sync_find_amount_of_steps_to_reach_the_goal(node, mapping, instructions, step, range_len, arr, n, lock):
    # node, mapping, instructions, step, range_len, arr, n, lock = args
    for i in range(range_len):
        node = mapping[node][instructions[step % len(instructions)]]
        step += 1
        if node.endswith('Z'):
            # with lock:
            temp = arr[n]
            temp.add(step)
            arr[n] = temp
            all_steps = arr  # [step[0] for step in arr]
            intersection = all_steps[0].intersection(*all_steps)
            intersection = {i for i in intersection if i != 0}
            result = min(intersection) if intersection else 0
            if result != 0:
                return {result}


def find_amount_of_steps_to_reach_the_goal_part_4(input_text):
    lines = input_text.splitlines()
    instructions = [int(i) for i in lines[0].replace('L', '0').replace('R', '1')]
    mapping = {key: (l, r) for key, l, r in map(lambda x: re.findall(r'\w+', x), lines[2:])}
    nodes = [key for key, _ in mapping.items() if key.endswith('A')]
    nodes = nodes[:4]
    print(nodes)
    nodes_len = len(nodes)
    steps = [{0} for _ in range(nodes_len)]
    range_len = mapping.__len__() * 5_000_000_000
    pool = Pool()

    with Manager() as manager:
        arr = manager.list(steps)
        lock = manager.Lock()
        result = pool.starmap(sync_find_amount_of_steps_to_reach_the_goal,
                                [(nodes[i], mapping, instructions, max(steps[i]), range_len, arr, i, lock) for i in
                                 range(len(nodes))])
        # steps = result.get()
        pool.close()
        pool.join()
        all_steps = steps  # [step[0] for step in arr]
        intersection = result[0].intersection(*result)
        result = min(intersection) if intersection else 0

        return result


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
# print(find_amount_of_steps_to_reach_the_goal_part_1(sample2))
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

if __name__ == '__main__':
    freeze_support()
    print(find_amount_of_steps_to_reach_the_goal_part_4(sample3))
    with open('input.txt', 'r') as f:
        start_time = time.time()
        print(find_amount_of_steps_to_reach_the_goal_part_4(f.read()))
        print("Sync Time: %02d:%02d" % (divmod(time.time() - start_time, 60)))


# async def main() -> None:
#     # print(await find_amount_of_steps_to_reach_the_goal_part_2(sample3))
#     with open('input.txt', 'r') as f:
#         start_time = time.time()
#         print(await find_amount_of_steps_to_reach_the_goal_part_2(f.read()))
#         print("Async Time: %02d:%02d" % (divmod(time.time() - start_time, 60)))
#
# asyncio.run(main())
