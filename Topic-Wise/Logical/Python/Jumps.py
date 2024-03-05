n=11
pos=10

index=1
count=1
power=1


# def check(index,count,power):
while(index<n-1):
    if(index+power<n-1):
        if index == pos:
            print(count)
            break;

        else:
            index += power
            count += 1
            power += 1

    else:
        power = 1
        index -= 2
        print(count)



    # return count


# print(check(1,1,1))







