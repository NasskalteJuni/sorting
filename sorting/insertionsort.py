from bisect import bisect_left


def insertionsort(unsorted_list) -> list:
    if unsorted_list is None or len(unsorted_list) < 2:
        return unsorted_list

    sorted_last_index = 0
    for i in range(1, len(unsorted_list)):
        current = unsorted_list[i]
        if current < unsorted_list[sorted_last_index]:
            unsorted_list.insert(bisect_left(unsorted_list, current, 0, sorted_last_index), current)
            i += 1
            del unsorted_list[i]
            print(unsorted_list)

        sorted_last_index += 1

    return unsorted_list
