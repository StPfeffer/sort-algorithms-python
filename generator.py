from random import randint


def Generator(n: int) -> list:
    """
    Generates a sorted list of unique values, of length n.
    """
    length = n
    sorted_list = set()

    while len(sorted_list) < length:
        sorted_list.add(randint(-3 * length, 3 * length))

    sorted_list = list(sorted_list)

    return sorted_list
