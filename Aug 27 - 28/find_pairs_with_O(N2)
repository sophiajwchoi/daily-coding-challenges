#Print all positive integer solutions to the equations
#a ** 3 + b ** 3 = c ** 3 + d ** 3 where a,b,c,and d
#are integers between 1 and 1000.

from collections import defaultdict
def findPairs():
    n = 1000
    listMap = defaultdict(list)
    for c in range(1, n):
        for d in range(1, n):
            result = c ** 3 + d ** 3
            listMap[result].append((c,d))

    for x in listMap:
        for li in listMap[x]:
            print(li, end='')
        print()

