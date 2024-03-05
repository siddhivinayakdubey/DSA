# def calSumUtil(a, b, n, m):
#
#     sum = [0] * n
#     i = n - 1
#     j = m - 1
#     k = n - 1
#     carry = 0
#     s = 0
#
#     while j >= 0:
#         s = a[i] + b[j] + carry
#         sum[k] = (s % 10)
#         carry = s // 10
#
#         k -= 1
#         i -= 1
#         j -= 1
#     while i >= 0:
#         s = a[i] + carry
#         sum[k] = (s % 10)
#         carry = s // 10
#
#         i -= 1
#         k -= 1
#
#     ans = 0
#     if carry:
#         ans = 10
#     for i in range(n):
#         ans += sum[i]
#         ans *= 10
#
#     return ans // 10
#
a=[1,0,0]
b=[1]
# n=len(a)
# m=len(b)
# print(calSumUtil(a,b,n,m))
# print(sum(str(a)))
def khushi(a,b):
    num1=''
    num2=''
    for numbers in a:
        num1+=str(numbers)
    for numbers in b:
        num2+=str(numbers)

    final= int(num1)-int(num2)
    output = [int(x) for x in str(final)]
    return output

print(khushi(a,b))
