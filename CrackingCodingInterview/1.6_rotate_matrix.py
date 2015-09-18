"""
rotate an n by n matrix 90 degrees
"""

def rotate(matrix):
    matrix_new = copy.deepcopy(matrix)
    for i in xrange(size):
        for j in reversed(range(size)):
            matrix_new[i][size-1-j] = matrix[j][i]
    return matrix_new
