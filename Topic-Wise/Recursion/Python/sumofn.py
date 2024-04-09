sum=0
def sumofn(x):
    global sum
    if x != 0:

        sumofn(x-1)
        sum+=x
    return sum

if __name__ == '__main__':
    print(sumofn(5))
