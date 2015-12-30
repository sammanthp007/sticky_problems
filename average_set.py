class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def avgset(self, A):
        avg_set = {}
        set_of_A = set(A)
        power_set = self.power_set(A)
        total_avg = self.get_average(A)
        for subset in power_set:
            temp_average = self.get_average(subset)
            if temp_average == total_avg:
                compliment_set = set(subset)
                compliment_set = list(set_of_A - compliment_set)
                if len(subset) < len(compliment_set) and tuple(subset) not in avg_set:
                    avg_set[tuple(subset)] = compliment_set
                elif len(compliment_set) < len(subset) and tuple(compliment_set) not in avg_set:
                    avg_set[tuple(compliment_set)] = subset
        keys = list(avg_set.keys())
        keys.sort()
        res = []
        if len(list(keys)) > 1:
            a = list(keys[1])
            a.sort()
            res.append(a)
            a = list(avg_set[keys[1]])
            a.sort()
            res.append(a)
            return res
        return None

    def power_set(self, lis):
        res = [[]]
        for item in lis:
            temp_res = res[:]
            for subset in temp_res:
                res.append(subset + [item])
        return res
    
    def get_average(self, lis):
        if len(lis) == 0:
            return -1
        total_sum = sum(lis)
        return float(total_sum) / float(len(lis))

a = Solution()
lis = [ 47, 14, 30, 19, 30, 4, 32, 32, 15, 2, 6, 24 ]
print (a.avgset(lis))

print (a.get_average([9,15]))