#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'calculateMinHP' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

R = 3
C = 3


def calculateMinHP(grid, m=None, n=None):
    # Write your code here

    dp = [[0 for x in range(C + 1)]
          for y in range(R + 1)]
    m, n = R, C

    if grid[m - 1][n - 1] > 0:
        dp[m - 1][n - 1] = 1
    else:
        dp[m - 1][n - 1] = abs(grid[m - 1][n - 1]) + 1

    for i in range(m - 2, -1, -1):
        dp[i][n - 1] = max(dp[i + 1][n - 1] -
                           grid[i][n - 1], 1)
    for i in range(2, -1, -1):
        dp[m - 1][i] = max(dp[m - 1][i + 1] -
                           grid[m - 1][i], 1)

    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            min_grid_on_exit = min(dp[i + 1][j],
                                   dp[i][j + 1])
            dp[i][j] = max(min_grid_on_exit -
                           grid[i][j], 1)

    return dp[0][0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    m = int(input().strip())

    n = int(input().strip())

    cost = []

    for _ in range(m):
        cost.append(list(map(int, input().rstrip().split())))

    result = calculateMinHP(cost)

    fptr.write(str(result) + '\n')

    fptr.close()