##input: Two lists of integers
##output: The pair of values(one value in each list) with the smallest
##        (non-negative) difference.

def smallest_diff(a1, a2):
    
    pairs = []
    for x in a1:
        idx = (return_index(x, a2))
        pairs.append([x, a2[idx]])

    if len(pairs) == 0: ##if either a1 or a2 is empty
        return 

    min_pair = abs(pairs[0][0] - pairs[0][1])
    a = None
    b = None
    for x, y in pairs:
        if abs(x - y) <= min_pair:
            min_pair = abs(x - y)
            a = x
            b = y
    return (a, b)

def return_index(a, a2):
    return min(range(len(a2)), key=lambda i: abs(a2[i]-a))

def main():
    a = [1,5, 8, 9]
    b = [10]
    print(smallest_diff(a, b))
    b = [11]
    print(smallest_diff(a, b))
    b = [2,9]
    print(smallest_diff(a, b))
    b = [3]
    print(smallest_diff(a, b))
