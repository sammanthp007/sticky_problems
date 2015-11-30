def selectionsort(lis):
	smallest = 0
	for i in range(len(lis)):
		for nth in range(len(lis)):
			if lis[nth] <= lis[smallest]:
				a = lis[smallest]
				lis[smallest] = lis[nth]
				lis[nth] = lis[smallest]
				