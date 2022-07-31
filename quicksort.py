from generator import Generator


# Divides array into two partitions
def Partition(arr: list, low: int, high: int) -> int:
    pivot = arr[high] # Last element

    i = low - 1 # Pointer for greater element

    for j in range(low, high):
        # If the current element is less than or equal to the pivot
        if arr[j] <= pivot:
            i += 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    
    # Swap the pivot element with the greater element
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1 # Position where partition is done


def QuickSort(arr: list, low: int, high: int) -> list:
    if low < high:
        # Pivot index
        p = Partition(arr, low, high)

        QuickSort(arr, low, p - 1) # Left side
        QuickSort(arr, p + 1, high) # Right side

    return arr # Sorted list


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_array = QuickSort(arr, 0, len(arr) - 1)
    print(sorted_array)
