# TODO: count the number of insertions this algorithm makes

def insertionSort(lst):
    """Note: this function mutates its input list, hence has no return value"""
    for i in range(1, len(lst)):
        # Insert lst[i] into the sorted sublist lst[0:i] such that lst[0: i+1] is sorted
        cur = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > cur:
            lst[k+1] = lst[k]  # <======= PLACE A BREAKPOINT HERE
            k -= 1

        # insert cur into lst at index [k+1]
        lst[k+1] = cur


myList = [ 90, 77, 71, 68, 65, 62, 59, 48, 19, 5, -22, -30, -40, -43 ]

print("Before:", myList)

insertionSort(myList)

print("After: ", myList)
