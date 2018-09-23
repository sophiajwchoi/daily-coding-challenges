##Given an encoded string, return it's decoded string.
##
##The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
##
##You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
##
##Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
##
##Examples:
##
##s = "3[a]2[bc]", return "aaabcbc".
##s = "3[a2[c]]", return "accaccacc".
##s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

import re 

def decode_str(s):
    stack_char = []
    stack_num = []

    for x in s:
        return_str = ""
        if bool(re.match('[\d/-]+$', x)):   #Confirm if the char is a digit
            stack_num.append(x)
        elif x == "]":
            times = int(stack_num.pop())
            string = ""
            while stack_char[-1] != "[":
                string = stack_char.pop() + string
            return_str = string * times
            stack_char.pop()
            stack_char.append(return_str)
        elif bool(re.match(r'^[a-zA-Z]+$', x)):   #Confirm if the char is an alphabet
            stack_char.append(x)
        elif x == "[":
            stack_char.append(x)
        else:
            return False    ##Return False if invalid input
    strr = ""
    while stack_char:
        strr =stack_char.pop() + strr
    return strr
