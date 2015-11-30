# implement a heapsort for a list - [2,1,54,23,54,23,44,22,55,11,12]
class HeapSort(object):
    def __init__(self, lis):
        self.heap = [0]
        for item in lis:
            self.heap.append(item)
            self.__floatup(len(self.heap) - 1, lis)
            print "items and heap", item, self.heap

    def push(self, d, lis):
        lis.append(d)
        self.__floatup(len(lis) - 1, lis)
        return True

    def peek(self, lis):
        if len(lis) > 0:
            return lis[1]
        else:
            return False

    def pop(self, lis):
        # swaps the first and last, and bubblesdown the first element
        highest = False
        if len(lis) > 0:
            self.__swap(lis, 1, len(lis) - 1)
            highest = lis.pop()
            print "bubblesdown starts"
            self.__bubbledown(1, lis)
            print "bubblesdown ends"
        return highest

    def __swap(self, lis, indx1, indx2):
        lis[indx1], lis[indx2] = lis[indx2], lis[indx1]

    def __floatup(self, index, lis):
        parent = index // 2
        print "parent", self.heap[parent], "child", self.heap[index]
        if index <= 1:
            return
        if lis[index] > lis[parent]:
            self.__swap(lis, index, parent)
            self.__floatup(parent, lis)

    def __bubbledown(self, parent, lis):
        print "original list before bubblesdown", lis
        child = parent * 2
        largest_index = parent
        if parent <= len(lis) // 2:
            if (child < len(lis) - 1) and (lis[child] < lis[child + 1]):
                child = child + 1
                print "printing child", [lis[child]]
            if lis[child] > lis[parent]:
                largest_index = child

        if largest_index != parent:
            self.__swap(lis, parent, child)
            self.__bubbledown(child, lis)
        print (self.heap)

    def heapify(self, lis):
        # the process assumes that the structure is a heap except at the top
        self.__bubbledown(1, lis)
        return True

    def sort(self):
        count = 0
        final = len(self.heap) - 1
        lis = self.heap
        while count <= final:
            print ("original lis before anythin"), lis
            print (count)
            print "pop starts"
            highest = self.pop(lis)
            print "pop ends"
            print (highest)
            lis = lis[::-1]
            self.heapify(lis)
            print (self.heap)
            count += 1
        return self.heap


# unsorted = [45,34,54,65,23,53,63]
# heapsort = HeapSort(unsorted)
# # print (heapsort.sort())
print (0 & 10)