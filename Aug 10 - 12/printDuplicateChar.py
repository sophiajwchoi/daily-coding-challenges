def printDuplicateChar(string):
    char_dict = {}
    for c in string:
        if (char_dict.get(c) == None):
            key = c
            char_dict[key] = 0
        char_dict[c] = char_dict[c]+ 1
        
    for key in char_dict:
        if (char_dict.get(key) > 1):
            print(key)
