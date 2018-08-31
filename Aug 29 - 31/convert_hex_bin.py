## work in progress

def convert_hex_to_binary(hex_str):
    return_bin = 0
    for i in range(len(hex_str)):
        if hex_str[i] in ['A','B','C','D','E','F']:
            a = char_to_dec(x)
        hex_str[i]
        return_bin = a + return_bin
        
    return return_bin    

def dec_to_bin(digit):
    if digit == 0:
        return 0000
    while digit // 2 != 0:
        
        
def char_to_dec(hex_char):
    if hex_char == "A":
        return 10
    if hex_char == "B":
        return 11
    if hex_char == "C":
        return 12
    if hex_char == "D":
        return 13
    if hex_char == "E":
        return 14
    if hex_char == "F":
        return 15
