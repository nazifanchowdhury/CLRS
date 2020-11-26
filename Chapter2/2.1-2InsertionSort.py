# Rewrite the Insertion-Sort procedure to sort into nonincreasing instead of nondecreasing order

def insertionSortNonInc(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j = i 

        while j>0 and arr[j-1]<val:
            arr[j] = arr[j-1]
            j = j-1

        arr[j] = val
pass