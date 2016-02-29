
def cocktailsort(unsorted_list) -> list:
    up = range(len(unsorted_list)-1)
    swaps_left = True
    while swaps_left:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if unsorted_list[i] > unsorted_list[i+1]:
                    unsorted_list[i], unsorted_list[i+1] = unsorted_list[i+1], unsorted_list[i]
                    swapped = True
                swaps_left = swapped
    return unsorted_list