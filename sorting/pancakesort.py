

def pancakesort(unsorted_list):
    def flip(complete_list, start, end):
        if end is None:
            end = len(complete_list)
        partial_list = complete_list[start:end]
        partial_list.reverse()
        complete_list[start:end] = partial_list

    sorted = 0
    while sorted < len(unsorted_list):
        if unsorted_list[sorted] < unsorted_list[sorted+1]
            sorted+1
        else:
            flip(unsorted_list,sorted+1)

    return unsorted_list
