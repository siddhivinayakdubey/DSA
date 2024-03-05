count=0
a=['(',')',')','(','(',')']
n=len(a)
for i in range(0,n):
    if a[i]=='(' and a[i+1]==')':
        count+=1

print(count)