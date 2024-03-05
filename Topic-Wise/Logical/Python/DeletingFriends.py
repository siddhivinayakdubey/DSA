T=int(input())
for i in range(0,T):
    n,k = input().split()
    n=int(n)
    k=int(k)
    l = input()
    arr=list(map(int, l.split(" ")))

    while(k>0):
        for i in range(0, n - 2):
            if (arr[i] < arr[i + 1]):
                arr.pop(i)
                k -= 1
    print(arr)




