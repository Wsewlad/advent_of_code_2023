import functools


def find_rank_of_hand(hand: str, letters: list) -> int:
    """
    Checks what type of hand it is and returns the rank.
    ARGS:
        hand: string of cards
        letters: list of letters in order of strength
    RETURNS:
        rank: integer of rank of hand
    """
    if letters[-1] == "J":
        counts = [hand.count(letter) for letter in letters if hand.count(letter) > 1 and letter != "J"]
        j_count = hand.count("J")
        if len(counts) > 0:
            counts[0] += j_count
        elif len(counts) == 0 and j_count > 0:
            if j_count < 5:
                counts.append(j_count + 1)
            else:
                counts.append(j_count)
    else:
        counts = [hand.count(letter) for letter in letters if hand.count(letter) > 1]

    if 5 in counts:
        return 7
    elif 4 in counts:
        return 6
    elif 3 in counts and 2 in counts:
        return 5
    elif 3 in counts:
        return 4
    elif counts.count(2) == 2:
        return 3
    elif 2 in counts:
        return 2
    else:
        return 1


def compare(x, y, strength: list):
    """
    Compares two hands and returns 1 if x is stronger, -1 if y is stronger and 0 if they are equal.
    ARGS:
        x: tuple of hand, bid and rank
        y: tuple of hand, bid and rank
        strength: list of letters in order of strength
    RETURNS:
        integer: 1 if x is stronger, -1 if y is stronger and 0 if they are equal.
    """
    hand_x, rank_x = x[0::2]
    hand_y, rank_y = y[0::2]
    if rank_x == rank_y:
        for i in range(len(hand_x)):
            if strength.index(hand_x[i]) > strength.index(hand_y[i]):
                return -1
            elif strength.index(hand_x[i]) < strength.index(hand_y[i]):
                return 1
        return 0
    else:
        return rank_x - rank_y


def find_total_winnings(input_text: str) -> int:
    strength = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    hand_to_bid = [(line.split()) for line in input_text.splitlines()]
    hand_to_bid_with_rank = [(hand, int(bid), find_rank_of_hand(hand, strength)) for hand, bid in hand_to_bid]
    hand_to_bid_with_rank_sorted = sorted(
        hand_to_bid_with_rank, key=functools.cmp_to_key(lambda x, y: compare(x, y, strength)), reverse=True
    )
    return sum(
        [
            bid * (len(hand_to_bid_with_rank_sorted) - idx)
            for idx, (_, bid, _) in enumerate(hand_to_bid_with_rank_sorted)
        ]
    )


def find_total_winnings2(input_text: str) -> int:
    strength = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    hand_to_bid = [(line.split()) for line in input_text.splitlines()]
    hand_to_bid_with_rank = [(hand, int(bid), find_rank_of_hand(hand, strength)) for hand, bid in hand_to_bid]
    hand_to_bid_with_rank_sorted = sorted(
        hand_to_bid_with_rank, key=functools.cmp_to_key(lambda x, y: compare(x, y, strength)), reverse=True
    )
    return sum(
        [
            bid * (len(hand_to_bid_with_rank_sorted) - idx)
            for idx, (_, bid, _) in enumerate(hand_to_bid_with_rank_sorted)
        ]
    )


sample = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

print(find_total_winnings(sample))
with open("input.txt", "r") as f:
    print(find_total_winnings(f.read()))

print(find_total_winnings2(sample))
with open("input.txt", "r") as f:
    print(find_total_winnings2(f.read()))
