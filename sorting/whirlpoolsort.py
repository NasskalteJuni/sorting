# Defined my own sorting algorithm
# it is worse than bubblesort and gained the title or code EISA (Extremely Inefficient Sorting Algorithm)
# it was inspired by the process of sorting a deck of cards:
# one takes the first card and takes it for an already sorted list with the first element as this card
# and of course the last element as this card and the length 1
# now, one takes the next card. If it is less than the first card,
# one goes through the list until the next element is either not in order (less than the previous one)
# or larger than the first card of the list.
# this smaller, in order sublist is prepended to the sublist
# now one takes the next card after the sublist
# if it is bigger than the last element,
# one iterates from there over the list until the next card is not in order
# the list of in order, bigger cards is 'appended'
# if the next card cannot be placed in front or after the sorted list
# place the sorted list in the end of the whole list
# now, take again the first card as a list with the first element as this card
# and the last element as this card and do the procedure again
# the list will become a list of longer and bigger sorted parts
# in the end, there will be a run where everything can be prepended and appended and
# everything will be sorted after this

def __next_is_still_in_list(complete_list, index):
    return index+1 < len(complete_list)


def __next_is_in_order(complete_list, index):
    return complete_list[index] < complete_list[index+1]


def __next_is_less_than(complete_list, index, lessthan):
    return complete_list[index+1] <= lessthan


def __get_insert_list_index(complete_list, upper, lessthan=None):
    index = upper
    while __next_is_still_in_list(complete_list, index) and __next_is_in_order(complete_list, index) and \
            ((lessthan is None) or (lessthan is not None and __next_is_less_than(complete_list, index, lessthan))):
        index += 1
    return index


def __move_list_part_to_front(complete_list, lower, upper, to_move_end):
    tmp = []
    for i in range(upper+1, to_move_end+1):
        tmp.append(complete_list[i])
    for i in range(lower, upper+1):
        tmp.append(complete_list[i])
    for i in range(lower, to_move_end+1):
        complete_list[i] = tmp[i]
    return complete_list


def __next_is_bigger_than(complete_list, index, biggerthan):
    return complete_list[index+1] > biggerthan


def __move_sorted_to_end(complete_list, lower, upper):
    tmp = []
    for i in range(upper+1, len(complete_list)):
        tmp.append(complete_list[i])
    for i in range(lower, upper+1):
        tmp.append(complete_list[i])
    for i in range(0, len(complete_list)):
        complete_list[i] = tmp[i]
    return complete_list


def __is_not_sorted(unsorted_list):
    for i in range(0, len(unsorted_list)-1):
        if unsorted_list[i] > unsorted_list[i+1]:
            return True
    return False


def whirlpoolsort(unsorted_list) -> list:
    lower = 0
    upper = 0
    while __is_not_sorted(unsorted_list):
        next_index = upper+1
        if __next_is_still_in_list(unsorted_list, next_index):
            # check if the element after the upper end is less than the value of the lower end
            if __next_is_less_than(unsorted_list, upper, unsorted_list[lower]):
                # get the last index of a list in order that is still smaller than the lower end
                stop_index = __get_insert_list_index(unsorted_list, next_index, unsorted_list[lower])
                # move the sorted list in front of the lower end
                __move_list_part_to_front(unsorted_list, lower, upper, stop_index)
            # check if the element after the upper end is bigger than the value of the upper and
            elif __next_is_bigger_than(unsorted_list, upper, unsorted_list[upper]):
                # get the last index of a list in order
                stop_index = __get_insert_list_index(unsorted_list, next_index)
                # the new upper end of the sorted list is now the index of the last element in order
                upper = stop_index
            # if the next element is neither lower than the lower end element nor bigger than the upper element
            # (i.e.: that the elements value is to put somewhere in between the upper or lower end):
            else:
                # move the sorted part to the end so that the next element is the new first element/ new sorted list
                # (sorted list with the length 1...)
                __move_sorted_to_end(unsorted_list, lower, upper)
                # the lower end is now the first element
                lower = 0
                # and the last element of the sorted list, the upper end is also this first element
                upper = 0

            # continue with this
