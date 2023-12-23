

def get_initialization_hash(initialization: str) -> int:
    result = 0
    for char in list(initialization):
        result += ord(char)
        result *= 17
        result %= 256
    return result


def get_hashes_sum(input_text: str) -> int:
    initializations = input_text.split(',')
    return sum([get_initialization_hash(h) for h in initializations])


sample = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

print(get_hashes_sum(sample))
with open('input.txt', 'r') as f:
    print(get_hashes_sum(f.read().strip()))
