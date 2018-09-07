## input type: str
## output type: str

def convert_hex_to_binary(hex_str):
    return_bin = ""
    for i in hex_str:
        if i in ['A','B','C','D','E','F']:
            i = char_to_dec(i)
        return_bin += dec_to_bin(i)
        
    return return_bin    

def dec_to_bin(digit):
    digit2 = int(digit)
    binary = ""
    while digit2 // 2 > 0:
        binary += str(digit2 % 2)
        digit2 = digit2 // 2
    binary = binary[::-1]     #Reverse the string
    if digit2 // 2 == 0 and len(binary) != 4:
        if digit2 == 1:
            binary = "1" + binary
        else:
            binary = "0" + binary
    offset = 4 - len(binary)
    binary = "0" * offset + binary
    
    return binary
        
        
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
