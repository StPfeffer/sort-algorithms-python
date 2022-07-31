from generator import Generator


def ShellSort(arr: list) -> list:
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap

        # Check from left to right
        while j < n:
            i = j - gap # Maintain gap value

            while i > 0:
                # If value on right side is greater than left don't swap
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                
                i = i - gap # Check left side
            j += 1
        gap = gap // 2

    return arr


if __name__ == '__main__':
    arr = Generator(1000)
    sorted_list = ShellSort(arr)
    print(sorted_list)
