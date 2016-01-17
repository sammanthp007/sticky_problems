# // Given two unsigned binary numbers expressed as strings of '1' and '0'
# // characters, return a string containing the sum of the numbers in the same
# // format.
# // 
# // Examples:
# // sum("1", "1") would return "10"
# // sum("1", "1011") would return "1100"

def add_two_binarys(bin1, bin2):
    len_bin1 = len(bin1)
    len_bin2 = len(bin2)
    if len_bin1 > len_bin2:
        bin2 = fill_up(bin2, len_bin1 - len_bin2) # this is the number of zero i want to add before
    elif len_bin2 > len_bin1:
        bin1 = fill_up(bin1, len_bin2 - len_bin1) # thie first rgument is which i want to be expanded
    
    curr_index = len(bin1) - 1
    add = ''
    carry_bit = 0
    temp_sum = 0
    while curr_index >= 0:
        if bin1[curr_index] == '0' and bin2[curr_index] == '0':
            temp_sum = 0 + carry_bit
            carry_bit = 0
        elif (bin1[curr_index] == '1' and bin2[curr_index] == '0') or (bin1[curr_index] == '0' and bin2[curr_index] == '1'):
            if carry_bit == 1:
                temp_sum = 0
                carry_bit = 1
            else:
                temp_sum = 1
                carry_bit = 0
        elif bin1[curr_index] == '1' and bin2[curr_index] == '1':
            if carry_bit == 0:
                temp_sum = 0
                carry_bit = 1
            else:
                temp_sum = 1
                carry_bit = 1      
        add = str(temp_sum) + add
        curr_index -= 1
    if carry_bit == 1:
        add = str(carry_bit) + add
    return add

def fill_up(string, num):
    for i in range(num):
        string = '0' + string
    return string

print (add_two_binarys('1', '0'))