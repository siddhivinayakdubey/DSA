n=6
count=0

for i in range(1,n+1):
    if(n%i==0):
        count+=1
        print(i)

if count>=3:
    print("not prime")
else:
    print('prime')
