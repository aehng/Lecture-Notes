# TODO: count the number of swaps this algorithm makes

def selectionSort(lst):
    """Note: this function mutates its input list, hence has no return value"""
    for i in range(len(lst) - 1):
        # find the smallest value in lst
        minIdx = i
        minVal = lst[i]

        for j in range(i + 1, len(lst)):
            if minVal > lst[j]:
                minVal = lst[j]
                minIdx = j

        # Swap minimum value w/lst[i], if needed
        if minIdx != i:
            lst[minIdx] = lst[i]  # <======= PLACE A BREAKPOINT HERE
            lst[i] = minVal


myList = [ 90, 77, 71, 68, 65, 62, 59, 48, 19, 5, -22, -30, -40, -43 ]

print("Before:", myList)

selectionSort(myList)

print("After: ", myList)
