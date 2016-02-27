
def bubblesort(unsorted_list) -> list:

    def __swap(unsorted_list, a, b):
        tmp = unsorted_list[a]
        unsorted_list[a] = unsorted_list[b]
        unsorted_list[b] = tmp

    length = len(unsorted_list)

    if length < 2:
        return unsorted_list

    for i in range(1, len(unsorted_list)):
        in_order = True
        for j in range(1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[j-1]:
                in_order = False
                __swap(unsorted_list, j, j-1)
        if in_order:
            print("could leave early after "+str(i)+" round")
            return unsorted_list

    return unsorted_list



