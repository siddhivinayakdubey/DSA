arr=[2,5,3,7,4,0,9]
Ea=[]
Oa=[]
for i in range(0,len(arr),2):
    Ea.append(arr[i])
for j in range(1,len(arr),2):
    Oa.append(arr[j])

Ea=sorted(Ea)
Oa=sorted(Oa)
print(Ea)
print(Oa)
print(Ea[len(Ea)-2]+Oa[1])