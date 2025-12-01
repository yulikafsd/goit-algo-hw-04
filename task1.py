import random
import timeit


def bubbble_sort(list):
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
    return list


def selection_sort(list):
    for i in range(len(list)):
        min_ind = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_ind]:
                min_ind = j
        list[i], list[min_ind] = list[min_ind], list[i]
    return list


def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[len(list) // 2]
    left = [num for num in list if num < pivot]
    middle = [num for num in list if num == pivot]
    right = [num for num in list if num > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    merged = []
    left_ind = 0
    right_ind = 0

    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] <= right[right_ind]:
            merged.append(left[left_ind])
            left_ind += 1
        else:
            merged.append(right[right_ind])
            right_ind += 1

    while left_ind < len(left):
        merged.append(left[left_ind])
        left_ind += 1

    while right_ind < len(right):
        merged.append(right[right_ind])
        right_ind += 1

    return merged


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def counting_sort(arr, position):
    size = len(arr)
    output = [0] * size
    count = [0] * 10

    # Рахунок входжень певного розряду
    for i in range(0, size):
        index = arr[i] // position % 10
        count[index] += 1

    # Оновлення count[i] так, щоб він показував позицію наступного входження своєї цифри
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Побудова вихідного масиву
    i = size - 1
    while i >= 0:
        index = arr[i] // position % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]


def radix_sort(arr):
    # Визначення максимального числа для визначення кількості розрядів
    max_num = max(arr)
    position = 1
    # Виконання counting_sort для кожного розряду
    while max_num // position > 0:
        counting_sort(arr, position)
        position *= 10
    return arr


def python_sort(arr):
    return arr.sort()


def python_sorted(arr):
    return sorted(arr)


funcs = [
    bubbble_sort,
    insertion_sort,
    selection_sort,
    quick_sort,
    merge_sort,
    shell_sort,
    radix_sort,
    python_sort,
    python_sorted,
]


lengths = [10, 100, 5000, 10000, 50000]  # number of numbers in an array
arrays = {N: random.choices(range(0, 201), k=N) for N in lengths}  # create arrays


if __name__ == "__main__":

    # Print header
    print(f"{'Function':>15}", end="")
    for N in lengths:
        print(f"{N:>12}", end="")
    print()

    # Test algorithms
    for func in funcs:
        print(f"{func.__name__:>15}", end="")
        for N in lengths:
            arr = arrays[N].copy()
            start = timeit.default_timer()
            func(arr)
            end = timeit.default_timer()
            print(f"{end - start:12.6f}", end="")
        print()
