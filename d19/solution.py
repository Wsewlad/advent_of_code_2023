

def apply_rule(message: dict, rule_key: str, rules: dict) -> bool:
    """
    Return True if the message is accepted by the rule, False otherwise.
    ARGS:
        message: dict, the message to check
        rule_key: str, the key of the rule to apply
        rules: dict, the rules to apply
    Returns:
        bool, True if the message is accepted by the rule, False otherwise
    """
    actions = {
        'R': lambda x: False,
        'A': lambda x: True,
    }
    rule = rules[rule_key]
    for r in rule:
        if '>' in r:
            field, value_and_action = r.split('>')
            value, action = value_and_action.split(':')
            if field in message:
                if int(message[field]) > int(value):
                    return actions.get(action, lambda x: apply_rule(x, action, rules))(message)
        elif '<' in r:
            field, value_and_action = r.split('<')
            value, action = value_and_action.split(':')
            if field in message:
                if int(message[field]) < int(value):
                    return actions.get(action, lambda x: apply_rule(x, action, rules))(message)
        elif r == 'A':
            return True
        elif r == 'R':
            return False
        else:
            return apply_rule(message, r, rules)


def apply_rule_iterative(message: dict, rule_key: str, rules: dict) -> bool:
    """
    Return True if the message is accepted by the rule, False otherwise.
    ARGS:
        message: dict, the message to check
        rule_key: str, the key of the rule to apply
        rules: dict, the rules to apply
    Returns:
        bool, True if the message is accepted by the rule, False otherwise
    """
    actions = {
        'R': lambda x: False,
        'A': lambda x: True,
    }
    rule_stack = [rule_key]
    while rule_stack:
        current_rule = rule_stack.pop()
        rule = rules[current_rule]
        for r in rule:
            if '>' in r:
                field, value_and_action = r.split('>')
                value, action = value_and_action.split(':')
                if field in message:
                    if int(message[field]) > int(value):
                        if action in actions.keys():
                            return actions[action](message)
                        else:
                            rule_stack.append(action)
                            break
            elif '<' in r:
                field, value_and_action = r.split('<')
                value, action = value_and_action.split(':')
                if field in message:
                    if int(message[field]) < int(value):
                        if action in actions.keys():
                            return actions[action](message)
                        else:
                            rule_stack.append(action)
                            break
            elif r == 'A':
                return True
            elif r == 'R':
                return False
            else:
                rule_stack.append(r)
                break


def sum_message(message: dict) -> int:
    """
    Return the sum of the values of the message.
    ARGS:
        message: dict, the message to sum
    Returns:
        int, the sum of the values of the message
    """
    return sum(int(v) for v in message.values())


def get_sum_of_accepted_ratings(input_text: str) -> int:
    """
    Return the sum of the ratings of the accepted messages.
    ARGS:
        input_text: str, the input text
    Returns:
        int, the sum of the ratings of the accepted messages
    """
    rules, messages = input_text.split('\n\n')
    rules = {
        rule.split('{')[0]: rule.split('{')[1].split('}')[0].strip().split(',')
        for rule in rules.split('\n')
    }
    messages = [message.replace('{', "").replace('}', "").split(',') for message in messages.split('\n')]
    messages = [dict([m.split('=') for m in message if '=' in m]) for message in messages]
    return sum(sum_message(message) for message in messages if apply_rule_iterative(message, 'in', rules))


def get_sum_of_accepted_ratings_part2(input_text: str) -> int:
    rules, _ = input_text.split('\n\n')
    rules = {
        rule.split('{')[0]: rule.split('{')[1].split('}')[0].strip().split(',')
        for rule in rules.split('\n')
    }
    messages = (
        {'x': x, 'm': m, 'a': a, 's': s}
        for x in range(1, 4001)
        for m in range(1, 4001)
        for a in range(1, 4001)
        for s in range(1, 4001)
    )
    return sum(sum_message(message) for message in messages if apply_rule(message, 'in', rules))


sample = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

print(get_sum_of_accepted_ratings(sample))
with open('input.txt', 'r') as f:
    print(get_sum_of_accepted_ratings(f.read()))

print(get_sum_of_accepted_ratings_part2(sample))
with open('input.txt', 'r') as f:
    print(get_sum_of_accepted_ratings_part2(f.read()))
