from itertools import permutations


def bogosort(unsorted_list) -> list:

    def __is_sorted(possibly_sorted_list) -> bool:
        if possibly_sorted_list is None or len(possibly_sorted_list) == 0:
            return True

        for index in range(1, len(possibly_sorted_list)):
            if possibly_sorted_list[index] < possibly_sorted_list[index-1]:
                return False
        return True

    for permutation in permutations(unsorted_list):
        if __is_sorted(unsorted_list):
            return unsorted_list
        else:
            unsorted_list[0:len(unsorted_list)] = permutation
