# Design an algorithm that determines the maximum profit that could have been made by buying and then selling a single share over a given day range, subject to the contraint that the buy and the sell have to take place at the start of the day. (This algorithm may be needed to backtest a trading strategy.)

# input: highest_array, lowest_array, start_prices_array


# The actual question is:
# Given a list, what is the biggest difference between two numbers such that the lower value is indexed before the higher value:

# input: lis
# output: res, an integer

# working:
# take the forst two numbers fro  the lsoit, and put then in a nother lisise that new list like a quie. bbut only queue if wother the next mumber is less than the smaller number aor bigger than the smaler nybmer/
# lis[0] -> count = 0, the number of elements in my new list;
# population_phase:
# i = 0
# while i < len(lis):
#     if lis[i] > queue[0]:
#         queue.append(lis[i])
#         break
#     if i + 1 == len(lis):
def return_best_stock_profit(lis):
    res = lis[1] - lis[0]
    bigger_num = lis[0]
    smaller_num = lis[0]
    # searching for the smaller number loop
    for i in range(len(lis)):
        for j in range(i,len(lis)):
            if lis[j] > lis[i]:
                if res < lis[j] - lis[i]:
                    res = lis[j] - lis[i]
    if res <= 0:
        return 0
    return (res)

lis = [5,4,3,2, 22]
print (return_best_stock_profit(lis))

def return_besT_stock(lis):
    max_diff = 0
    min_index = 0
    for i in range(len(lis)):
        if lis[i] < lis[min_index]:
            min_index = i
        temp_diff = lis[i] - lis[min_index]
        if temp_diff > max_diff:
            max_diff = temp_diff
    return max_diff

print (return_besT_stock(lis))

def return_best_stock_rec(lis):
    length = len(lis)
    if length == 0:
        return 0
    first_arr_best = return_best_stock_profit(lis[:length//2])
    second_arr_best = return_best_stock_profit(lis[length//2:])
    if first_arr_best > second_arr_best:
        res = first_arr_best
    else:
        res = second_arr_best
    low = min(lis[:length//2])
    hig = max(lis[length//2:])
    if hig - low > res:
        res = hig - low
    return res

print (return_best_stock_rec(lis))