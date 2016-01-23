

----------------------------------------------------------

Given a square matrix, output its diagonals. E.g.,

3  4  9 10
5  2  1  7
7  6  2  1
4  0  1  2

Output: [3, 4, 5, 9, 2, 7, 10, 1, 6, 4, 7, 2, 0, 1, 1, 2]

input -> lis -> [[2,3,4],[3,4,5]]

working -> 
[0,0],  [0, 1],[1,0],   [0,2],[1,1][2,0],  [0,3],[1,2],[2,1],[3,0],     [1,3], [2,2],   [3,1]       [2,3],[3,2],[3,3] 
[0,0], [first, last], [last, first], [first, last],[second, second],[last, first]

#subproblem :get the diagonal of each square matrix
#take the square matrix
#first row; last row

def get_diagonals(lis):
res_lis =[]
for i in range(0, 2 * len(lis)):
# {0,1,2,3,4, 5,6} - number of times
    start_row = 0 4
    start_col = i 0
    
    while start_col >= 0:
        if start_col >= len(lis) or start_row >= len(lis):
            start_col -= 1
            start_row += 1
            continue
        res_lis.append(lis[start_row][start_col])
        start_row += 1
        start_col -= 1
return res_lis

# [3, 4, 5, 9, 2, 7, 10, 1, 6, 4, 7, 2, 0,  ]
3  4  9 10
5  2  1  7
7  6  2  1
4  0  1  2

N * N -

# {[0,0],[0,1],[0,2],[0,3],[0,4]
