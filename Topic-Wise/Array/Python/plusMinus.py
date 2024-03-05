def plusMinus(arr):
    # Write your code here
    n=len(arr)
    zeroes = 0
    pos = 0
    neg = 0

    for i in range(0, n):
        if (arr[i] == 0):
            zeroes += 1
        elif (arr[i] > 0):
            pos += 1
        elif (arr[i] < 0):
            neg += 1


    fp = '{0:.6f}'.format(pos / n)
    fn = '{0:.6f}'.format(neg / n)
    fo = '{0:.6f}'.format(zeroes / n)

    return fp,fn,fo
arr=[-4,3,-9,0,4,1]
print(plusMinus(arr))
# arr=[-4,3,-9,0,4,1]
# n=len(arr)
# zeroes = 0
# pos = 0
# neg = 0
#
# for i in range(0, n):
#     if (arr[i] == 0):
#         zeroes += 1
#     elif (arr[i] > 0):
#         pos += 1
#     elif (arr[i] < 0):
#         neg += 1
#
# print(zeroes," ",pos," ",neg)
# fp = '{0:.6f}'.format(pos / n)
# fn = '{0:.6f}'.format(neg / n)
# fo = '{0:.6f}'.format(zeroes / n)
# print(fp," ",fn," ",fo)