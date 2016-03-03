def slowersort(unsorted_list, i=None, j=None):
    if i is None:
        i = 0
    if j is None:
        j = len(unsorted_list) - 1
    if i < j:
        m = (i + j) // 2
        slowersort(unsorted_list, i, m)
        slowersort(unsorted_list, m + 1, j)
        if unsorted_list[m] > unsorted_list[j]:
            for k in range(m, j):
                unsorted_list[k], unsorted_list[k + 1] = unsorted_list[k + 1], unsorted_list[k]
        slowersort(unsorted_list, i, j - 1)