# rotate using circular array concept
def rotate_array_different_list(lis, rotation_value):
    res = []
    for index in range(len(lis)):
        res.append(lis[(index + rotation_value) % len(lis)])
    return res

# rotate using slices:
def rotate_array_using_slicing(lis, rotation_value):
    return lis[rotation_value:] + lis[:rotation_value]