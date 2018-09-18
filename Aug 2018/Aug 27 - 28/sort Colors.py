##Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
##
##Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
##
##Note: You are not suppose to use the library's sort function for this problem.
##
##Example:
##
##Input: [2,0,2,1,1,0]
##Output: [0,0,1,1,2,2]


def sort_colours(arr):
    i = 0
    j = len(arr) - 1

    for l in range(j + 1):
        while arr[l] == 2 and l < j:
            swap(arr, l, j)
            j -= 1
        while arr[l] == 0 and l > i:
            swap(arr, l, i)
            i += 1
    return arr

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
