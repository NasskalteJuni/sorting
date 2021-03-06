from math import ceil


def heapsort(lst):

    def __siftdown(lst, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    for start in range(ceil((len(lst)-2)/2), -1, -1):
        __siftdown(lst, start, len(lst) - 1)


    for end in range(len(lst)-1, 0, -1):
        lst[end], lst[0] = lst[0], lst[end]
        __siftdown(lst, 0, end - 1)

    return lst
