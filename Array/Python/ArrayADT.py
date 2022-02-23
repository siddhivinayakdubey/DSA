# inserting
temp=[]
arr=[1,2,3,4,5,3]
n=len(arr)

for i in arr:
    x=arr.count(i)
    if(x>1):
        temp.append(arr[i])
        x=0
print(temp)

