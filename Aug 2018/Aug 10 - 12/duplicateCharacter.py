def uniqueCharacter(s):
    charSet = {}
    status = True
    for char in s:
        if (char not in charSet):
            charSet[char] = 0
        charSet[char] += 1
        if (charSet[char] > 1):
            status = False
    return status
