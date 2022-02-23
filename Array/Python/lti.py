n=9
arr=[10,5,20,20,4,5,2,25,1]

maxi=arr[0]
mini=arr[0]
maxcount=0
mincount=0

for i in range(1,n):
    if(arr[i]>maxi):
        maxi=arr[i]
        maxcount+=1
    if(arr[i]<mini):
        mini=arr[i]
        mincount+=1
print(maxcount,mincount)