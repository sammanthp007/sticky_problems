A = 3

temp = ((A & 1<<i) >> i)&1
ret = ret | temp << (31-i)