def strCompression(s):
    charMap = {}
    prev = s[0]
    returnStr = ""
    for i in range(len(s)):
        if (s[i] not in charMap):
            charMap[s[i]] = 0
        charMap[s[i]] += 1
        if (i == len(s) - 1 or s[i] != prev):
            returnStr += prev+str(charMap[prev])
            prev = s[i]
    return returnStr
