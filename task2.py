# Python sort method
# def merge_k_lists(lists):
#     n = len(lists)
#     merged = [num for lst in lists for num in lst]
#     return sorted(merged)


# Merge sort algorithm
def merge_k_lists(lists):
    if not lists:
        return []

    while len(lists) > 1:
        merged_list = []

        for i in range(0, len(lists), 2):
            first = lists[i]
            second = lists[i + 1] if (i + 1) < len(lists) else []
            merged_list.append(merge(first, second))

        lists = merged_list

    return lists[0]


def merge(lst_one, lst_two):
    merged = []
    left_ind = 0
    right_ind = 0

    while left_ind < len(lst_one) and right_ind < len(lst_two):
        if lst_one[left_ind] <= lst_two[right_ind]:
            merged.append(lst_one[left_ind])
            left_ind += 1
        else:
            merged.append(lst_two[right_ind])
            right_ind += 1

    while left_ind < len(lst_one):
        merged.append(lst_one[left_ind])
        left_ind += 1

    while right_ind < len(lst_two):
        merged.append(lst_two[right_ind])
        right_ind += 1

    return merged


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

if __name__ == "__main__":
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
