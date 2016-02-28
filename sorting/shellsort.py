

def shellsort(unsorted_list):
    inc = len(unsorted_list) // 2
    while inc:
        for i, current_elem in enumerate(unsorted_list):
            while i >= inc and unsorted_list[i - inc] > current_elem:
                unsorted_list[i] = unsorted_list[i - inc]
                i -= inc
            unsorted_list[i] = current_elem
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
