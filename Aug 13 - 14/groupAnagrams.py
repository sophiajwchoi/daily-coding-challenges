def groupAnagrams(arr):
    group = {}
    for i in arr:
        sorted_str = ''.join(sorted(list(i)))
        if sorted_str not in group:
            group[sorted_str] = list()
        group[sorted_str].append(i)
    return group_array(group)


def group_array(hashList):
    returnList = list()
    for i in hashList:
        returnList += hashList[i]
    return returnList


##input: a = ['ABC', 'AB', 'BA', 'BAC', 'DD', 'LMO', 'FF', 'OML']
##output: ['ABC', 'BAC', 'AB', 'BA', 'DD', 'LMO', 'OML', 'FF']
