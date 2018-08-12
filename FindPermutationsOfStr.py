def main():
    string = "ABC"
    n = len(string)
    a = list(string)
    permute (a, 0, n - 1)

def permute(listOfChar, index, lastIndex):
    if (index == lastIndex):
        permutation = ''.join(listOfChar)
        print(permutation)
    else:
        for i in range(index, lastIndex + 1):
            listOfChar[index], listOfChar[i] = listOfChar[i], listOfChar[index]
            permute(listOfChar, index + 1, lastIndex)
            listOfChar[i], listOfChar[index] = listOfChar[index], listOfChar[i]
