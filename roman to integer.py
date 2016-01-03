to_int = {'I' : 1,
          'V' : 5,
          'X' : 10,
          'L' : 50,
          'C' : 100,
          'D' : 500,
          'M' : 1000
          }

# IV -> smaller, larger -> return larger - smaller
# XI -> larger, smaller -> return larger + smaller -> add the first, then
# vv

def roman_to_int(roman):
    if len(roman) == 1:
        return to_int[roman]
    elif len(roman) < 1:
        return -1
    current_ptr = 0
    next_ptr = 1
    # return value initialize
    res = 0
    # case 0: when the next_ptr >= len(roman): return current_ptr
    while True:
        if current_ptr >= len(roman):
            return res
        elif next_ptr >= len(roman) and current_ptr < len(roman):
            res += to_int[roman[current_ptr]]
            current_ptr += 1
    # case 1: when current_ptr > next_ptr -> just add to the result the value at the current_ptr, move current_ptr one step forward and the next_ptr another step forward
        elif to_int[roman[current_ptr]] >= to_int[roman[next_ptr]]:
            res += to_int[roman[current_ptr]]
            current_ptr += 1
            next_ptr += 1
    # case 2: when current_ptr < next_ptr -> temp = next_ptr - current_ptr; res += temp; current_ptr = next_ptr + 1; next_ptr = next_ptr + 2
        elif to_int[roman[current_ptr]] < to_int[roman[next_ptr]]:
            temp = to_int[roman[next_ptr]] - to_int[roman[current_ptr]]
            res += temp
            current_ptr += 2
            next_ptr += 2
    return res

roman = 'CCCXLII'
print (roman_to_int(roman))

# <<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def int_to_roman (integer):
    parts = []
    for letter, value in TABLE:
        while value <= integer:
            integer -= value
            parts.append(letter)
    return ''.join(parts)
TABLE=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]

a = 342
print (int_to_roman(a))

# integer = 342
# 342 - 100 = 242 -> C