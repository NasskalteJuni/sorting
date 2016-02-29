

def pancakesort(unsorted_list) -> list:
    def flip(complete_list, start, end=None):
        if end is None:
            end = len(complete_list)
        partial_list = complete_list[start:end]
        partial_list.reverse()
        complete_list[start:end] = partial_list

    def index_of_min(complete_list, start, end):
        min_found = complete_list[start]
        index = start
        for i in range(start, end):
            if complete_list[i] < min_found:
                min_found = complete_list[i]
                index = i
        return index

    sorted_index = 0
    while sorted_index < len(unsorted_list):
        min_index = index_of_min(unsorted_list, sorted_index, len(unsorted_list))
        if min_index != sorted_index:
            flip(unsorted_list, min_index)
            flip(unsorted_list, sorted_index)
        sorted_index += 1
    return unsorted_list


