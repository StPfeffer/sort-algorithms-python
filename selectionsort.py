from generator import Generator


def SelectionSort(arr: list) -> list:
    for i in range(len(arr)):
        min_i = i # minimum element in remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
        
        # Swap the minimum element with the first element
        arr[i], arr[min_i] = arr[min_i], arr[i]

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = SelectionSort(arr)
    print(sorted_list)
