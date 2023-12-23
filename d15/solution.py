
def get_initialization_hash(initialization: str) -> int:
    """
    Cuclulates the hash of the initialization string
    ARGS:
        initialization: str - the initialization string
    RETURNS:
        int - the hash of the initialization string
    """
    result = 0
    for char in list(initialization):
        result += ord(char)
        result *= 17
        result %= 256
    return result


def get_hashes_sum(input_text: str) -> int:
    """
    Calculates the sum of the hashes of the initializations
    ARGS:
        input_text: str - the input text
    RETURNS:
        int - the sum of the hashes of the initializations
    """
    initializations = input_text.split(',')
    return sum([get_initialization_hash(h) for h in initializations])


def find_the_focusing_power_of_box(box: list, box_number: int) -> int:
    """
    Calculates the focusing power of the box
    ARGS:
        box: list - the box
        box_number: int - the number of the box
    RETURNS:
        int - the focusing power of the box
    """
    result = 0
    for i, (label, focal_length) in enumerate(box):
        result += box_number * (i + 1) * int(focal_length)
    return result


def find_the_focusing_power_of_configuration(input_text: str) -> int:
    """
    Calculates the focusing power of the configuration
    ARGS:
        input_text: str - the input text
    RETURNS:
        int - the focusing power of the configuration
    """
    boxes = [list() for _ in range(256)]
    initializations = input_text.split(',')
    for initialization in initializations:
        if '=' in initialization:
            label, focal_length = initialization.split('=')
            label_hash = get_initialization_hash(label)
            for i, l in enumerate(boxes[label_hash]):
                if l[0] == label:
                    boxes[label_hash][i] = (label, focal_length)
                    break
            else:
                boxes[label_hash].append((label, focal_length))
        elif '-' in initialization:
            label, focal_length = initialization.split('-')
            label_hash = get_initialization_hash(label)
            boxes[label_hash] = [x for x in boxes[label_hash] if x[0] != label]
        else:
            raise ValueError('Wrong initialization format')
    return sum([find_the_focusing_power_of_box(box, i + 1) for i, box in enumerate(boxes)])


sample = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

print(get_hashes_sum(sample))
with open('input.txt', 'r') as f:
    print(get_hashes_sum(f.read().strip()))

print(find_the_focusing_power_of_configuration(sample))
with open('input.txt', 'r') as f:
    print(find_the_focusing_power_of_configuration(f.read().strip()))
