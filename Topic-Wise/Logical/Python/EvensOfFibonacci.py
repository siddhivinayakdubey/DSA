n=9
for i in range(0,n):
    if i+(i+1)==i+2:
        print("The series is:" +str(i+2))
        i+=1
    else:
        i+=1
        continue
