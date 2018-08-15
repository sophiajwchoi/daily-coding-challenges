def peaksAndValleys(arr):
    peaks = []
    valleys = []
    rest = []
    inc = 0
    for i in range(len(arr) - 1):     
        trend = 0
        if arr[i] < arr[i + 1]:
            trend = 1
        elif arr[i] > arr[i + 1]:
            trend = - 1
        else:
            trend = 0
        if i == 0:
            if inc + trend == 1:
                valleys.append(arr[i])
            elif inc + trend == 0:
                rest.append(arr[i])
            else:
                peaks.append(arr[i])
            continue
        if inc + trend == 0:
            if (inc < 0 and trend > 0):
                valleys.append(arr[i])
            else:
                peaks.append(arr[i])
        else:
            rest.append(arr[i])
        inc = trend
    if trend > 0:
        peaks.append(arr[-1])
    elif trend == 0:
        rest.append(arr[-1])
    else:
        valleys.append(arr[i])
    returnList = []

    while len(peaks) != 0 or len(valleys) != 0:
        if len(peaks) != 0:
            p = peaks.pop()
            returnList.append(p)
        if len(valleys) != 0:
            v = valleys.pop()
            returnList.append(v)
    for x in rest:
        returnList.append(x)

    return returnList

        
            
    
