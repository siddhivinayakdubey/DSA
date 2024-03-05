arr=[8,3,6,4,6,5,6,8,2,7]

n=len(arr)
Max=max(arr)
H=[0]*(Max+1)

for i in range(0,n):
    H[arr[i]]+=1

for i in range(0,Max):
    if(H[i]>1):
        print("number: "+str(i)+" in count: "+str(H[i]))



