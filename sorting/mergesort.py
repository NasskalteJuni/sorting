

def mergesort(unsorted_list):

    def __merge_in_place(complete_list, start, mid, end):
        left = complete_list[start:mid]
        right = complete_list[mid:end]
        index_left = 0
        index_right = 0
        k = start
        for l in range(k,end):
            if index_right >= len(right) or (index_left < len(left) and left[index_left] < right[index_right]):
                complete_list[l] = left[index_left]
                index_left += 1
            else:
                complete_list[l] = right[index_right]
                index_right += 1

    def __recursive_split_and_merge(complete_list, left, right):
        if right - left > 1:
            mid = int((left + right) / 2)
            __recursive_split_and_merge(complete_list, left, mid)
            __recursive_split_and_merge(complete_list, mid, right)
            __merge_in_place(complete_list, left, mid, right)

    if unsorted_list is None or len(unsorted_list) == 1:
        return unsorted_list
    else:
        return __recursive_split_and_merge(unsorted_list, 0, len(unsorted_list))




