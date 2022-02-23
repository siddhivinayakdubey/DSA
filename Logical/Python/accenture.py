def funn(a,b,c):
    for c in range(4,5):

        b=(c+a)&b

         if((b^a)<c):

            a=(a+b)+b

            b=(b&a)+b
        else:

            b=c+c

            b=a+a

    return a+b

print(funn(1,5,9))