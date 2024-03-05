def DetectPerfectNumber(n):
    Sum=0
    for i in range(1,n):

        if(n%i==0):
            Sum+=i

    if(Sum==n):
        return 1
    else:
        return Sum


def maxlength(s):
    n = len(s)
    ans = 0;
    for i in range(n):

        # Count the number of contiguous 1's
        if (s[i] == '1'):
            count = 1
            j = i + 1
            while (j <= n - 1 and s[j] == '1'):
                count += 1
                j += 1
            ans = max(ans, count)
    return ans

print(maxlength('10111010101011'))


