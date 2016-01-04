# Numbers are randomly generated and stored into an (expanding) array. How would you keep track of the median?
questions:
# are the new numbers added one at a time? -> yes
Can we insert the new number where ever we want to -> if no then go on but if yes, then we can insert it such that the array remains sorted and if it is placed in the medians position, then we can 
median = (len(lis) + 1) // 2

input -> median, new_number
I would put this array in a heap. such that the elements lower than the min is in a min-heap and the elements higher than the median is in the max-heap.

