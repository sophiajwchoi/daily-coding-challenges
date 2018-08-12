def highestOccurredChar(string):
    char_dict = {}
    for s in string:
        if (char_dict.get(s) == None):
            char_dict[s] = 0
        char_dict[s] = char_dict.get(s) + 1

        counter = 0
    char = []
    for s in char_dict:
        if (char_dict.get(s) >= counter):
            counter = char_dict.get(s)
            char.append(s)
    print(char)
