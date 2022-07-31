from generator import Generator


def BubbleSort(arr: list) -> list:
    n = len(arr)

    for i in range(n):
        # Last i elements are already in place
        for j in range(n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = BubbleSort(arr)
    print(sorted_list)
