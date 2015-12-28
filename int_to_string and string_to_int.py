def integer_to_string(x):
    is_negative = False
    if x == 0:
        return chr(ord('0'))
    if x < 0:
        is_negative = True
        x = -x
    representation = ''
    while x != 0:
        representation = chr(ord('0') + x % 10) + representation
        x = x // 10
    if is_negative:
        representation = '-' + representation
    return representation

a = 234
print (a, type(a))
res = integer_to_string(a)
print (res, type(res))

def string_to_integer(string):
    is_negative = string[0] == '-'
    res = 0
    if is_negative:
        string = string[1:]
    for i in string:
        if ord(i) < 48 or ord(i) > 57:
            return 'invalid'
        res = res * 10 + (ord(i) - 48)
    if is_negative:
        res = res - (2 * res)
    return res

print(string_to_integer('-234'))
