from sorting.bubblesort import bubblesort
from sorting.pancakesort import pancakesort
from sorting.cocktailsort import cocktailsort
from sorting.quicksort import quicksort
from sorting.shellsort import shellsort
from sorting.bogosort import bogosort
from sorting.combsort import combsort
from sorting.cyclesort import cyclesort
from sorting.insertionsort import insertionsort
from sorting.mergesort import iterative_mergesort
from sorting.gnomesort import gnomesort
from sorting.heapsort import heapsort
from sorting.selectionsort import selectionsort
from sorting.slowsort import slowersort
import functools
import inspect


def sorting_algorithm(wrapped):
   @functools.wraps(wrapped)  # optional - make wrapper look like wrapped
   def wrapper(*args):
        print('inside wrapper:')
        fsig = inspect.signature(wrapped)
        parameters = ', '.join('{}={}'.format(*pair)
                               for pair in zip(fsig.parameters, args))
        print('  wrapped call to {}({})'.format(wrapped.__name__, parameters))
        for parameter in fsig.parameters.values():
            print("  {} param's annotation: {!r}".format(parameter.name,
                                                         parameter.annotation))
        result = wrapped(*args)
        print('  returning {!r} with annotation: {!r}'.format(result,
                                                         fsig.return_annotation))
        return result
   return wrapper

@sorting_algorithm
def my_alg(unsorted_list):
    return unsorted_list

def get_algorithmlist():
    algorithms = [
        ("bubble sort", bubblesort),
        ("pancake sort", pancakesort),
        ("cocktail sort", cocktailsort),
        ("merge sort", iterative_mergesort),
        ("quick sort", quicksort),
        ("gnome sort", gnomesort),
        ("heap sort", heapsort),
        ("selection sort", selectionsort),
        ("shell sort", shellsort),
        ("bogo sort", bogosort),
        ("comb sort", combsort),
        ("cycle sort", cyclesort),
        ("insertion sort", insertionsort),
        ("slow sort", slowersort)
    ]
    algorithms.sort(key=lambda tpl: tpl[0])
    return algorithms

print(sorting_algorithm([1]))