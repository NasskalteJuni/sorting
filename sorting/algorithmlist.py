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
from sorting.smoothsort import smoothsort
from sorting.snailsort import snailsort
from sorting.americanflagsort import american_flag_sort


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
        ("slow sort", slowersort),
        ("smooth sort", smoothsort),
        ("snail sort", snailsort),
        ("american flag sort", american_flag_sort)
    ]
    algorithms.sort(key=lambda tpl: tpl[0])
    return algorithms
