def checkPermutation(s, t):
    sPerm = findChar(s)
    tPerm = findChar(t)

    for x in sPerm:
        if x not in tPerm:
            return False
        elif sPerm[x] != tPerm[x]:
            return False
    return True

def findChar(string):
    perm = {}
    for char in string:
        if char not in perm:
            perm[char] = 0
        perm[char] += 1
    return perm
