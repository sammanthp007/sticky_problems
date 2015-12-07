# Given 2 non negative integers m and n, find gcd(m, n)

# GCD of 2 integers m and n is defined as the greatest integer g such that g is a divisor of both m and n.
# Both m and n fit in a 32 bit signed integer.

# euclidean way:
# 1) GCD(A, 0) = A
# 2) GCD(0, B) = B
# 3) GCD(A,B) = GCD(B, A % B)
def gcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    if n2 == 0:
        return n1
    return gcd(n2, n1 % n2)

# and for lcm:
# lcm = num1 * num2 divided by their greatest common factor
def lcm(n1, n2):
    return (n1 * n2 / gcd(n1, n2))
