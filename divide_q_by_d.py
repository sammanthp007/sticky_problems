# compute x/y

# Given two positive integers x and y, how would you compute x/y if the only operators you can use are addition, subtraction, and shifting?

def division(dividend, divisor):
    quotient = dividend
    remainder = 0
    res = 0
    while quotient >= divisor:
        quotient -= divisor
        res += 1
    return res

# print (division(212,21))

def div_rec(quotient, divisor):
    if quotient < divisor:
        return 0
    if quotient == divisor:
        return 1
    return 1 + div_rec(quotient - divisor, divisor)

def div_logn(quotient, divisor, k):
    if quotient < divisor:
        return 0
    if quotient >= (divisor << k):
        return (1 << k) + div_logn(quotient - (divisor << k), divisor, k + 1)
    if quotient == divisor:
        return 1
    return 1 + div_logn(quotient - divisor, divisor, abs(k - 1))

def divide_q_by_d(q, d):
    res = 0
    while q >= d:
        # by how much?
        pow = 1
        while q >= d << pow:
            pow += 1
        pow_we_increase_by = pow - 1
        res += 1 << pow_we_increase_by
        q -= d << pow_we_increase_by
    return res

print (divide_q_by_d(32232422323,4))
a = 1234366
b = 33
# print (div_rec(a, b))

print (div_logn(a,b, 1))