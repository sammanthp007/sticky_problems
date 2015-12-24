# look-and-say problem

def look_and_say(number):
    res_lis = ['1', '11']
    res = 0
    # str_lis = [str(i) for i in res_lis]
    for num in range(number):
        last = res_lis[-1]
        i = 0
        temp = ''
        while i < len(last):
            count = 1
            while i + 1 < len(last) and last[i] == last[i + 1]:
                count += 1
                i += 1
            temp += str(count) + last[i]
            i += 1
        res_lis.append(temp)
    return int(res_lis[number])
    # return a number
    
print (look_and_say(9))