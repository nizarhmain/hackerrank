

matrix = [[11, 2, 10], [4, 5, 6], [4, 8, -12]]


def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(len(arr)):
        left += arr[len(arr) - i - 1][i]
        right += arr[i][i - len(arr)]
    return abs(left - right) 

# right_to_left(matrix)
# left_to_right(matrix)
print(diagonalDifference(matrix))
