

def next_is_still_in_list(complete_list, index):
    return index+1 < len(complete_list)

test1 = [1, 3, 7, 6, 3, 5]
print("-------------------------")
print("test1")
print("Assert True: "+str(next_is_still_in_list(test1, 4)))
print("Assert False: "+str(next_is_still_in_list(test1, 5)))
print("-------------------------")



def next_is_in_order(complete_list, index):
    return complete_list[index] < complete_list[index+1]

test2 = [1, 3, 7, 6, 3, 5]
print("-------------------------")
print("test2")
print("Assert True: "+str(next_is_in_order(test2, 1)))
print("Assert False: "+str(next_is_in_order(test2, 2)))
print("-------------------------")


def next_is_less_than(complete_list, index, lessthan):
    return complete_list[index+1] <= lessthan


def get_insert_list_index(complete_list, upper, lessthan=None):
    index = upper
    while next_is_still_in_list(complete_list, index) and next_is_in_order(complete_list, index) and \
            ((lessthan is None) or (lessthan is not None and next_is_less_than(complete_list, index, lessthan))):
        index += 1
    return index


test3 = [1, 3, 7, 6, 3, 5]
print("-------------------------")
print("test3")
print("Assert 5: "+str(get_insert_list_index(test3, 3)))
print("Assert 2: "+str(get_insert_list_index(test3, 0)))
print("Assert 2: "+str(get_insert_list_index(test3, 2)))
print("Assert 1: "+str(get_insert_list_index(test3, 0, 4)))
print("Assert 2: "+str(get_insert_list_index(test3, 0, 8)))
print("Assert 2: "+str(get_insert_list_index(test3, 2, 8)))
print("-------------------------")


def move_list_part_to_front(complete_list, lower, upper, to_move_end):
    tmp = []
    for i in range(upper+1, to_move_end+1):
        tmp.append(complete_list[i])
    for i in range(lower, upper+1):
        tmp.append(complete_list[i])
    for i in range(lower, to_move_end+1):
        complete_list[i] = tmp[i]
    return complete_list

test4 = [1, 3, 7, 6, 3, 5]
test5 = [1, 3, 7, 6, 3, 5]
print("-------------------------")
print("test4")
print("Assert [6,1,3,7,3,5]: "+str(move_list_part_to_front(test4, 0, 2, 3)))
print("Assert [6,3,5,1,3,7]: "+str(move_list_part_to_front(test5, 0, 2, 5)))
print("-------------------------")


def next_is_bigger_than(complete_list, index, biggerthan):
    return complete_list[index+1] > biggerthan


def move_sorted_to_end(complete_list, lower, upper):
    tmp = []
    for i in range(upper+1, len(complete_list)):
        tmp.append(complete_list[i])
    for i in range(lower, upper+1):
        tmp.append(complete_list[i])
    for i in range(0, len(complete_list)):
        complete_list[i] = tmp[i]
    return complete_list


test6 = [1, 3, 7, 6, 2, 5]
test7 = [1, 3, 7, 6, 2, 5]
print("-------------------------")
print("test5")
print("Assert [6,2,5,1,3,7]: "+str(move_sorted_to_end(test6, 0, 2)))
print("Assert [7,6,2,5,1,3]: "+str(move_sorted_to_end(test7, 0, 1)))
print("-------------------------")

def is_not_sorted(unsorted_list):
    for i in range(0, len(unsorted_list)-1):
        if unsorted_list[i] > unsorted_list[i+1]:
            return True
    return False


def whirlpoolsort(unsorted_list) -> list:
    lower = 0
    upper = 0
    index = 0
    while is_not_sorted(unsorted_list) and index < 50:
        print(unsorted_list)
        next_index = upper+1
        if next_is_still_in_list(unsorted_list, next_index):
            # check if the element after the upper end is less than the value of the lower end
            if next_is_less_than(unsorted_list, upper, unsorted_list[lower]):
                # get the last index of a list in order that is still smaller than the lower end
                stop_index = get_insert_list_index(unsorted_list, next_index, lower)
                # move the sorted list in front of the lower end
                move_list_part_to_front(unsorted_list, lower, upper, stop_index+1)
            # check if the element after the upper end is bigger than the value of the upper and
            elif next_is_bigger_than(unsorted_list, upper, upper):
                # get the last index of a list in order
                stop_index = get_insert_list_index(unsorted_list, next_index)
                # the new upper end of the sorted list is now the index of the last element in order
                upper = stop_index
            # if the next element is neither lower than the lower end element nor bigger than the upper element
            # (i.e.: that the elements value is to put somewhere in between the upper or lower end):
            else:
                # move the sorted part to the end so that the next element is the new first element/ new sorted list
                # (sorted list with the length 1...)
                move_sorted_to_end(unsorted_list, lower, upper-1)
                # the lower end is now the first element
                lower = 0
                # and the last element of the sorted list, the upper end is also this first element
                upper = 0

            # continue with this
        index += 1

testlist = [1, 3, 9, 8, 2, 5, 4, 7, 6]
whirlpoolsort(testlist)
print(testlist)