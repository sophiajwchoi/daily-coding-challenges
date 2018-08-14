def searchInRotatedArr(arr, left, right, x):
    mid = (left + right) // 2
    if (x == arr[mid]): #if the item found
        return mid

    if (right < left): #if the item is not found
        return -1

    if arr[left] < a[mid]: #search right recursively
        if (arr[left] <= x and x < arr[mid]):
            searchInRotatedArr(arr, left, mid - 1, x)
        else:
            searchInRotatedArr(arr, mid + 1, right, x)
    if arr[right] > a[mid]: #search left
        if (arr[right] >= x and x > arr[mid]):
            searchInRotatedArr(arr, mid + 1, right, x)
        else:
            searchInRotatedArr(arr, left, mid - 1, x)
            
    elif a[left] == a[mid]:
        if a[mid] != a[right]:
            searchInRotatedArr(arr, mid + 1, right, x)
        else:
            result = searchInRotatedArr(arr, left, mid - 1, x)
            if result == -1:
                searchInRotatedArr(arr, mid + 1, right, x)
            else:
                return result
    return -1
