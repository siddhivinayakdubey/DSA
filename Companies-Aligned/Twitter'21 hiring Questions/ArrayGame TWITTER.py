
#### with built in numbers
nummbers=[3,4,6,6,3]
def countmoves(nummbers):
    n=len(nummbers)
    sums=sum(nummbers)
    chhota=min(nummbers)
    ops=sums-(n*chhota)
    return ops


###### FASTER
def countmoves(numbers):
    n=len(numbers)
    sums=0
    chhota=numbers[1]
    if(n<1):
        return 0

    for i in range(0,n):
        sums+=numbers[i]
        if numbers[i]<chhota:
            chhota=numbers[i]
    return sums-(n*chhota)


print(countmoves(nummbers))