from itertools import chain

def bucketsort(unsorted_list) -> list:
    minimum = min(unsorted_list)
    maximum = max(unsorted_list)

    # change these functions to use the bucket list as a hash table
    def __get_key(value):
        return value - minimum

    def __get_empty_list():
        return [[] for x in range(minimum, maximum+1)]

    buckets = __get_empty_list()

    for i in range(0, len(unsorted_list)):
        buckets[__get_key(unsorted_list[i])].append(unsorted_list[i])

    return list(chain.from_iterable(buckets))
