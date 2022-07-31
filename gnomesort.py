from generator import Generator


def GnomeSort(arr: list) -> list:
    n = len(arr)
    i = 0

    while i < n:
        if i == 0:
            i += 1

        if arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = GnomeSort(arr)
    print(sorted_list)
