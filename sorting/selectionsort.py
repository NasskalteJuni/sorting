
def selectionsort(unsorted_list) -> list:
    sorted_last_index = 0

    def __index_of_sublist_min(complete_list, start, end) -> int:
        minimum = complete_list[start]
        minimum_index = start
        for i in range(start, end):
            if complete_list[i] < minimum:
                minimum = complete_list[i]
                minimum_index = i
        return minimum_index

    def __swap(complete_list, a, b):
        tmp = complete_list[a]
        complete_list[a] = complete_list[b]
        complete_list[b] = tmp

    for i in range(0, len(unsorted_list)):
        index_next = __index_of_sublist_min(unsorted_list, sorted_last_index, len(unsorted_list))
        if index_next != sorted_last_index:
            __swap(unsorted_list, sorted_last_index, index_next)
        sorted_last_index += 1

    return unsorted_list
