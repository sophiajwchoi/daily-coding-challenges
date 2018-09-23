import re

def isDigits(string):
    print(bool(re.match('[\d/-]+$', string)))
