##For simplicity, consider the data in the range 0 to 9. 
##Code obtained from en.wikibooks.org and modified
##
##Time complexity: O(m)
##
##Space complexity: Sorts in-place with the auxillary counting array
##                  O(len(arr)) => O(m) where m is the length of the array
def countSort(arr):
    m = 9 + 1       #9 is the max val of the arr
    count = [0] * m

    for i in arr:
        count[i] += 1
    j = 0
    
    for a in range(m):
        for c in range(count[a]):
            arr[j] = a
            j += 1
    return (arr)
