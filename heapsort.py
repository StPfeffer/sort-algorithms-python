from generator import Generator


def HeapSort(arr: list) -> list:
    def Heapify(arr:list, n: int, i: int):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # See if left child of root exists and is greater than root
        if left < n and arr[largest] < arr[left]:
            largest = left

        # Right child
        if right < n and arr[largest] < arr[right]:
            largest = right

        # Change root if needed
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            # Heapify the root
            Heapify(arr, n, largest)

    
    n = len(arr)

    # Build a maxheap
    for i in range(n // 2 - 1, -1, -1):
        Heapify(arr, n, i)
    
    # Extract elements 1 by 1
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        Heapify(arr, i, 0)

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = HeapSort(arr)
    print(sorted_list)
