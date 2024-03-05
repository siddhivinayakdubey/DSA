def CountOfOddSum(a, n):
    dp = [[0 for i in range(2)]
          for i in range(n)]
    cnt = [[0 for i in range(2)]
           for i in range(n)]

    # Initialize two array with 0
    for i in range(n):
        for j in range(2):

            # if element is even
            if (a[i][j] % 2 == 0):

                # store count of even
                # number in i'th pair
                cnt[i][0] += 1

            # if the element is odd
            else:

                # store count of odd
                # number in i'th pair
                cnt[i][1] += 1

    # Initial state of dp array
    dp[0][0] = cnt[0][0]
    dp[0][1] = cnt[0][1]

    for i in range(1, n):
        # dp[i][0] = total number of ways
        # to get even sum upto i'th pair
        dp[i][0] = (dp[i - 1][0] * cnt[i][0] +
                    dp[i - 1][1] * cnt[i][1])

        # dp[i][1] = total number of ways
        # to odd even sum upto i'th pair
        dp[i][1] = (dp[i - 1][0] * cnt[i][1] +
                    dp[i - 1][1] * cnt[i][0])

    # dp[n - 1][1] = total number of ways
    # to get odd sum upto n'th pair
    return dp[n - 1][1]


# Driver code
a = [[1,2], [2,5],[1,4],[1,3]]
n = len(a)

ans = CountOfOddSum(a, n)

print(ans)