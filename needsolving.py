

#Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. 
#Note: This is not a necessarily a binary search tree

def find(tree, node1, node2):
    
    
psudo:
    see if one of the node is a child of the other
    if not:
        go to the parent of one of the node, and see to the other side if there is another node
        
        
        
# nodes : value, leftptr, rightptr

#On an old cell phones, users typed on a numeric keyboard and the phone would provide a list of words that matched these numbers. Each digit mapped to a set of 0-4 letters.Implement an algorithm to return a list of matching words, given a sequence of digits. You are provided a list of valid words (provided in whatever data structure you'd like). The mapping is sent to you as a picture in facebook:

#input: 8733
#output: tree, used

t9letters = {null, null, {'a', 'b', 'c'}, {'d', 'e', 'f'}, {'g','h','i'}, {'j','k','l'}, {'m','n','o'}, }


print getvalidT9words("8733", setwordlist)
setwordlist = {"tree", "used", "prek""shak", "interview", "ok"}

# Problem 6.3 : For each of the following, A is an integer array of length n.
# (1.) Compute the maximum value of (A[j0] − A[i0]) + (A[j1] − A[i1]), subject to i 0 < j 0 < i 1 < j 1 .
# (2.) Compute the maximum value of Submission(k−1 t=0) (A[jt ] − A[it]), subject to i 0 < j 0 < i 1 < j 1 <···< i k−1 < j k−1 . Here k is a fixed input parameter.
# (3.) Repeat Problem (2.) when k can be chosen to be any value from 0 to n/2.