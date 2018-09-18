##Swap a number in place

def number_swapper(a, b):
    a += b
    b = a - b
    a = a - b

    return (a, b)
