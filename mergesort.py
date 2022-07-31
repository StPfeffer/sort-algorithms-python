from generator import Generator


def MergeSort(arr: list) -> list:
    if len(arr) > 1:
        midpoint = len(arr) // 2

        # Dividing the array elements
        left = arr[:midpoint]
        right = arr[midpoint:]

        MergeSort(left)
        MergeSort(right)

        i = j = k = 0

        # Copy data to temp arrays left and right
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = MergeSort(arr)
    print(sorted_list)
