# Convert Base
# Write a function that performs base conversion. Specifically, the input is an integer base b1, a string s, representing an integer x in base b1, and another integer base b2; the output is the string representating the integer x in base b2. Assume 2 <= b1, b2 <= 16. Use "A" to represent 10, "B" for 11,..., and "F" for 15.

# working:
#     convert the given string to base 10
#     covert the decimal to the required base 

def convert_to_base10(string, base):
    last_position = len(string) - 1
    res = 0
    for digit in string:
        res += int(digit) * (base ** last_position)
        last_position -= 1
    return str(res)

def convert_decimal_to_base(string, base):
    converter = '0123456789ABCDEF'
    num = int(string)
    res = ''
    while num:
        res = converter[num % base] + res
        num = num // base
    return res
    
def convert_base(string, b1, b2):
    return convert_decimal_to_base(convert_to_base10(string, b1), b2)

print (convert_base('32', 10, 2))
