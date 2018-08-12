import re

def isDigits(string):
    a = "I love u"
    print(a.split())
    for s in a:
        print(s)
    print(bool(re.match('[\d/-]+$', string)))
