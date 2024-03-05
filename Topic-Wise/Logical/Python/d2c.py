from math import sqrt


# Utility function to check whether a
# number is prime or not
def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    k = int(sqrt(n)) + 1
    for i in range(5, k, 6):
        if (n % i == 0 or n % (i + 2) == 0):
            return False

    return True


# Function to check whether given number
# has three distinct factors or not
def isThreeDisctFactors(n):
    # Find square root of number
    sq = int(sqrt(n))

    # Check whether number is perfect
    # square or not
    if (1 * sq * sq != n):
        return False

    # If number is perfect square, check
    # whether square root is prime or
    # not
    if (isPrime(sq)):
        return True
    else:
        return False


# Driver program
if __name__ == '_main_':

    num = int(input())

    arr = []
    for i in range(0, num):
        x = int(input())
        arr.append(x)

    for i in range(0, num):
        count = 0
        for j in range(0, arr[i]):
            if (isThreeDisctFactors(j)):
                count = count + 1
        i = i + 1
        print(count)