def quicksort(unsorted_list) -> list:

    def partition(complete_list, start, end):
            pivot = complete_list[end]
            bottom = start-1
            top = end

            done = False
            while not done:

                while not done:
                    bottom += 1

                    if bottom == top:
                        done = True
                        break

                    if complete_list[bottom] > pivot:
                        complete_list[top] = complete_list[bottom]
                        break

                while not done:
                    top -= 1

                    if top == bottom:
                        done = True
                        break

                    if complete_list[top] < pivot:
                        complete_list[bottom] = complete_list[top]
                        break

            complete_list[top] = pivot
            return top

    def quicksort_recursion(complete_list, start, end):
        if start < end:
            split = partition(complete_list, start, end)
            quicksort_recursion(complete_list, start, split - 1)
            quicksort_recursion(complete_list, split + 1, end)
        else:
            return

    if unsorted_list is None or len(unsorted_list) < 2:
        return unsorted_list

    return quicksort_recursion(unsorted_list, 0, len(unsorted_list)-1)
