list1 = [2,3,57,5,43,14, 14,12,15,32,47,35,23]
list2 = [4,7,2,5,45,12,21,6,8]


def get_common_member_using_dictionary(list1, list2):
	result = []
	list1_dic = {}
	# making a dictionary of items in list1
	for item in list1:
		val = list1_dic.get(item,0)
		if val:
			list1_dic[item] = val + 1
		else:
			list1_dic[item] = 1

	for item in list2:
		# val = list1_dic.get(item, 0)
		if item in list1_dic:
			result.append(item)
		else:
			continue
	return result

print (get_common_member_using_dictionary(list1, list2))

def get_common_member_using_set(list1, list2):
	set1 = {item for item in list1}
	set2 = {item for item in list2}
	common_items = set1 & set2
	common_list = [item for item in common_items]
	return (common_list)

# print (get_common_member_using_set(list1, list2))