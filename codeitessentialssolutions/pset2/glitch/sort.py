# INSERTION SORT
def insertionSort(array, n):
    for i in range(1, n + 1):
        j = i
        while (j != 0 and sum(array[j - 1]) > sum(array[j])):
            temp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = temp
            j -= 1
    return

# MERGE SORT

def merge(array, lo, hi):
    mid = int((hi + lo)/2) 
    # print("merging from {} to {}, mid: {}".format(lo, hi, mid))
    aux = [0] * (hi - lo + 1)
    
    i = lo
    j = mid + 1
    tracker = 0
    
    while(i < mid + 1 and j < hi + 1):
        if sum(array[i]) >= sum(array[j]):
            aux[tracker] = array[j]
            j += 1
            tracker += 1
            
        elif sum(array[i]) < sum(array[j]):
            aux[tracker] = array[i]
            i += 1
            tracker += 1

    while (i < mid + 1):
        aux[tracker] = array[i]
        i += 1
        tracker += 1

    while (j < hi + 1):
        aux[tracker] = array[j]
        j += 1
        tracker += 1

    # print(aux)
    for i in range(lo, hi + 1):
        array[i] = aux[i - lo]

def mergeSort(array, lo, hi):
    if (lo >= hi):
        return
        
    mid = int((hi + lo)/2)
    mergeSort(array, lo, mid)
    mergeSort(array, mid + 1, hi)
    merge(array, lo, hi)

sample = [(0, 0, 0)]