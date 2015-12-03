def reverse_list_in_place(lis, start_index, end_index):
    while (start_index < end_index):
        temp = lis[start_index]
        lis[start_index] = lis[end_index]
        lis[end_index] = temp
        start_index += 1
        end_index -= 1

def rotate_array_in_place(lis, rotation_value):
    k_index = len(lis) - rotation_value
    reverse_list_in_place(lis, 0, len(lis) - 1)
    reverse_list_in_place(lis, k_index, len(lis) - 1)
    reverse_list_in_place(lis, 0, k_index - 1)