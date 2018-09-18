def combinationalSum(arr, x):
    arr = sorted(list(set(arr)))
    res=[]
    findNumber(arr, x, 0, res, [])
    return res
    
def findNumber(arr, x, i, res, curr):
    if x == 0:
        res.append(curr)
        return

    for i in range(i, len(arr)):
        if x < arr[i]:
            return
        findNumber(arr,x-arr[i],i,res,curr+[arr[i]])
        
