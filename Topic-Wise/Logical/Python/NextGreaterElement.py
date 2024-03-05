temp=[]
n = 121
no=n

while((int)(n)>0):
    r=(int)(n%10)

    temp.append(r)
    n = n / 10


print(temp)
temp.sort(reverse=True)
print(temp)

strint = [str(int) for int in temp]


strint = "".join(strint)
strint=(int)(strint)



if(strint==no):
    print("-1")




print(type(strint))