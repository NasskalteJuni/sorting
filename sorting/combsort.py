

def combsort(unsorted_list):

    gap = len(unsorted_list)
    shrink_factor = 1.3
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap/shrink_factor))
        swaps = False
        for i in range(0, len(unsorted_list) - gap):
            j = i + gap
            if unsorted_list[i] > unsorted_list[j]:
                unsorted_list[i], unsorted_list[j] = unsorted_list[j], unsorted_list[i]
                swaps = True
    return unsorted_list
