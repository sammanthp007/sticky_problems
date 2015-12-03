def reverse_list_in_place(lis, start_index, end_index):
    while (start_index < end_index):
        temp = lis[start_index]
        lis[start_index] = lis[end_index]
        lis[end_index] = temp
        start_index += 1
        end_index -= 1