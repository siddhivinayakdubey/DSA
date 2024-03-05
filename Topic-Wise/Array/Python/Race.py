temp=[]
n=5
arr=[[1,7],[2,4],[6,9],[3,8],[5,10]]
x=1
var=0

for x in range(1,n):
    for i in range(0,n-1):
        j=0
        if(x>=arr[i][j] and x<=arr[i][j+1]):
            var+=1
        else:
            continue
    temp.append(var)
    var=0
temp.sort()
o=len(temp)
print(temp[o-1])


