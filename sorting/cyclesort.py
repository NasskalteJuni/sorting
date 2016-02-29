

def cyclesort(unsorted_list) -> list:

    for cycleStart, item in enumerate(unsorted_list):
        position = cycleStart
        for item2 in unsorted_list[cycleStart + 1:]:
            if item2 < item:
                position += 1

        if position == cycleStart:
            continue

        while item == unsorted_list[position]:
            position += 1
        unsorted_list[position], item = item, unsorted_list[position]

        while position != cycleStart:
            position = cycleStart
            for item2 in unsorted_list[cycleStart + 1:]:
                if item2 < item:
                    position += 1
            while item == unsorted_list[position]:
                position += 1
            unsorted_list[position], item = item, unsorted_list[position]
    return unsorted_list
