# TODO: count the number of swaps this algorithm makes

def bubbleSort(lst):
    """Note: this function mutates its input list, hence has no return value"""
    while True:
        swapped = False

        for k in range(len(lst) - 1):
            # Swap an item if it is greater than the value at its right
            if lst[k] > lst[k+1]:
                lst[k], lst[k+1] = lst[k+1], lst[k]  # <======= PLACE A BREAKPOINT HERE
                swapped = True

        # Make passes until no swaps are performed
        if not swapped:
            break


myList = [ 90, 77, 71, 68, 65, 62, 59, 48, 19, 5, -22, -30, -40, -43 ]

print("Before:", myList)

bubbleSort(myList)

print("After: ", myList)
