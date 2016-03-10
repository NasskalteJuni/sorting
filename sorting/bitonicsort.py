def bitonic_sort(unsorted_list, ascending):
    if len(unsorted_list)<=1:
        return unsorted_list
    else:
        first = bitonic_sort(unsorted_list[:len(unsorted_list) / 2], True)
        second = bitonic_sort(unsorted_list[len(unsorted_list) / 2:], False)
        return bitonic_merge(first + second, ascending)

def bitonic_merge(unsorted_list, ascending):
    # assume input x is bitonic, and sorted list is returned
    if len(unsorted_list) == 1:
        return unsorted_list
    else:
        bitonic_compare(unsorted_list, ascending)
        first = bitonic_merge(unsorted_list[:len(unsorted_list) / 2], ascending)
        second = bitonic_merge(unsorted_list[len(unsorted_list) / 2:], ascending)
        return first + second

def bitonic_compare(unsorted_list, ascending):
    dist = len(unsorted_list) / 2
    for i in range(dist):
        if (unsorted_list[i] > unsorted_list[i+dist]) == ascending:
            unsorted_list[i], unsorted_list[i + dist] = unsorted_list[i + dist], unsorted_list[i] #swap
