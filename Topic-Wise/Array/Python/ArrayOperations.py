
# for i in range(0,T):
#     n = int(input())
#     l = input()
#     print(l[::-1])

# b=[None]*n
#
# i=n-1
# for j in range(0,n):
#     b[j]=arr[i]
#     i-=1
# print(b)'

# i=0
# j=n-1
#
# while(i<=j):
#     arr[i],arr[j]=arr[j],arr[i]
#     i+=1
#     j-=1
#
# print(arr)


###### Left Shift
arr=[2,3,4,6,23,1]
n=len(arr)

for i in range(1,n):
    arr[i-1]=arr[i]
arr[n-1]=0

print(arr)
