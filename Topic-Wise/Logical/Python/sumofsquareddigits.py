n = 142
Sum=0
while ((int)(n) > 0):
    r = (int)(n % 10)
    Sum+=r*r
    n = n / 10

print(Sum)
