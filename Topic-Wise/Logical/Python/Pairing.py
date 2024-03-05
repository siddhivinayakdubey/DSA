# def pairing(n):
#     x=0
#     a=1
#     b=2
#     c=0
#     if n%2!=0:
#         x=1
#         return x
#     else:
#         for i in range(3,n):
#             c=b(i-1)*a
#             a=b
#             b=c
#
#         return c
#
#
# n = 6
# print(pairing(n))


def countFriendsPairings(n):
    dp = [0 for i in range(n + 1)]
    if(n%2!=0):
        x=1
        return 1
    else:
        # Filling dp[] in bottom-up manner using
        # recursive formula explained above.
        for i in range(n + 1):

            if (i <= 2):
                dp[i] = i
            else:
                dp[i] = dp[i - 1] + (i - 1) * dp[i - 2]

        return dp[n]




# Driver code
n = int(input())
print(countFriendsPairings(n))