c = "111110101"
d = "a101010101"




def binary_checker(c):
    for i in c:
        if i != "0" and i != "1":
            is_binary = False
            return is_binary
            break
    return True
# binary_checker(c)
def bin_to_hex(num):
    if binary_checker(num) is True:
        for i in range(1,len(num)+1):
            if (i + len(num)) % 4 == 0:
                zeros_to_be_added = i +len(num)
                break
        final_number = num.zfill((zeros_to_be_added))
        bin_to_hex_map = {
                    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
                    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
                    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
                }
                
                # Convert each group of 4 binary digits to hexadecimal
        hex_result = ''
        for i in range(0, len(final_number), 4):
            four_bits = final_number[i:i+4]
            print(four_bits)
            hex_result += bin_to_hex_map[four_bits]
        
        print("The hexadecimal representation is:", hex_result)
    else:
        print("The number does not look binary.")
bin_to_hex(c)
