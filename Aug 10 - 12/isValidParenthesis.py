def isValid(s):
    stack = []
    status = True;
    for char in s:
        if (char == '(' or char == '{' or char == '['):
            stack.append(char)
        else:
            topOfStack = stack.pop()
            if ((char ==')' and topOfStack != '(') or (char =='}' and topOfStack != '{') or (char ==']' and topOfStack != '[')):
                status = False
    if (len(stack) != 0):
        status = False
    return status
