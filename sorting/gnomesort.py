

def gnomesort(unsorted_list) -> list:

    def __swap(unsorted_list, a, b):
        tmp = unsorted_list[a]
        unsorted_list[a] = unsorted_list[b]
        unsorted_list[b] = tmp

    current_index = 0
    while current_index < len(unsorted_list)-1:
        if unsorted_list[current_index] <= unsorted_list[current_index+1]:
            current_index += 1
        else:
            __swap(unsorted_list, current_index, current_index+1)
            if current_index > 0:
                current_index -= 1

    return unsorted_list
