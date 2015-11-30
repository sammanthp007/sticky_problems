# let the given list be in lis

def bubble_sort(lis):
	for items in range(len(lis)):
		for nth in range(len(lis) - 1):
			if lis[nth] > lis[nth + 1]:
				a = lis[nth + 1]
				lis[nth + 1] = lis[nth]
				lis[nth] = a

a = [2,4,5,7,5,1,5,4,2,54,1,4,2]
# print a
bubble_sort(a)
print a