def sparseSearch(arr, s):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if arr[mid] != "":
            if arr[mid] == s:
                return mid
        if arr[left] == "" or arr[left] != s:
            left += 1
            print(left)
        else:
            return left
        
        if arr[right] == "" or arr[right] != s:
            right -= 1
            print(right)
        else:
            return right

    return -1
