def rev_string1(a):
    return_str = ""
    for i in range(-1, -len(a) - 1, -1):
        return_str += a[i]
    return return_str

        
def rev_string2(a):
    if len(a) == 0:
        return
     
    temp = a[0]
    rev_string2(a[1:])
    print(temp, end='')

def main():
    print(rev_string2("olleH"))
