##Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
##
##Example:
##
##Input: [-2,1,-3,4,-1,2,1,-5,4],
##Output: 6
##Explanation: [4,-1,2,1] has the largest sum = 6.


def max_sum_subarray(arr):
    curr_max = arr[0]
    total_max = arr[0]

    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max + arr[i])
        total_max = max(total_max, curr_max)

    return total_max


##Returning the contiguous subarray with the largest sum

def max_sum_subarray2(arr):

    curr_max = arr[0]
    total_max = arr[0]
    total = [arr[0]]
    curr = [arr[0]]

    for i in range(1, len(arr)):

        if arr[i] >= curr_max + arr[i]:
            curr_max = arr[i]
            curr = [arr[i]]
        else:
            curr_max = curr_max + arr[i]
            curr.append(arr[i])
            
        if total_max < curr_max:
            total_max = curr_max
            total = curr
            print(total)

            #debugging required


    return total
            
