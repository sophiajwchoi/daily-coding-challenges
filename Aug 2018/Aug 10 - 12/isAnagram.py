def isAnagram(str1, str2):
    str1 = replaceSpace(str1.lower())
    str2 = replaceSpace(str2.lower())
    status = True

    if (len(str1) != len(str2) or len(str1) == 0 or len(str2) == 0):
        status = False
        
    char_set = set()
    for char in str1:
        char_set.add(char)

        
    for char in str2:
        if (char in char_set == False):
            status = False

    if (status != False):
        print(True)
    else: print(status)

        
def replaceSpace(string):
    return string.replace(" ", "")

