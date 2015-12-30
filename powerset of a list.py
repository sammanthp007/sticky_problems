def powerset(lis):
    result = [[]]
    for item in lis:
        temp = result[:]
        for subset in temp:
            result.extend([subset + [item]])
    return result

print (powerset(lis))