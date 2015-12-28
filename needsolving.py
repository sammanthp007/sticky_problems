

#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
#Note: This is not a necessarily a binary search tree

# def find(tree, node1, node2):
    
    
# psudo:
#     see if one of the node is a child of the other
#     if not:
#         go to the parent of one of the node, and see to the other side if there is another node
        
        
        
# nodes : value, leftptr, rightptr

#On an old cell phones, users typed on a numeric keyboard and the phone would provide a list of words that matched these numbers. Each digit mapped to a set of 0-4 letters.Implement an algorithm to return a list of matching words, given a sequence of digits. You are provided a list of valid words (provided in whatever data structure you'd like). The mapping is sent to you as a picture in facebook:

#input: 8733
#output: tree, used

# t9letters = {null, null, {'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g','h','i'}, {'j','k','l'}, {'m','n','o'}, }


# print getvalidT9words("8733", setwordlist)
# setwordlist = {"tree", "used", "prek""shak", "interview", "ok"}

# A robot needs to travel along a path that includes several ascents and descents. When it goes up, it uses its battery to power the motor and when it descends, it recovers the energy which is stored in the battery. The battery recharging process is idea: on descending, every Joule of gravitational potential energy converts to a Joule of electrical energy which is stored in the battery. The battery has a limited capacity and once it reaches this capacity, the energy generated in descending is lost.

# Design an algorithm that takes a sequence of n three-dimensional coordinates to be traversed, and returns the minimum battery capacity needed to complete the journey. The robot begins with a fully charged battery.

# battery = 0
# case1: when you only descends:
#     if battery is 0: then do nothing
#     elif battery is negative: then add as much as until it is still less than 0
# case2: when you ascend, you need x energy
#     x = x - something
# your minimum amount is abs(battery)

def max_difference(lis):
    battery = 0
    initial_height = lis[0]
    for coordinates in lis:
        height_difference = initial_height - coordinates
        if height_difference > 0:
            if battery == 0:
                initial_height = coordinates
            else:
                battery += height_difference
                if battery > 0:
                    battery = 0
        else:
            battery -= height_difference
    return abs(battery)

lis=[3,4,5,6,2,4]
print (max_difference(lis))