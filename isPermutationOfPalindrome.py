def palindromePerm(s):
    s = s.lower().replace(" ","")
    charMap = {}
    count = 0
    for char in s:
        if (char not in charMap):
            charMap[char] = 0
        charMap[char] += 1
        if (charMap[char] % 2 == 0):
            count -= 1
        else:
            count += 1
    if count <= 1:
        return True
    else: return False
