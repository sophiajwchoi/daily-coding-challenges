###Given two sorted arrays, a and b, where a
###has a large enough buffer at the end to hold
###b. write a method to merge B into sorted order.

def insertionSort(a, b):
    a = a + b
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = key
    return a
            

###def optimizedSort(a, b): will be optimized shortly
 