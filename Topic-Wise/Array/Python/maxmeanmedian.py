def printMaxMedian(arr, n):
    # case when size of the array is odd
    if n % 2 != 0:
        maxElement = arr.index(max(arr))
        (arr[maxElement],
         arr[n // 2]) = (arr[n // 2],
                         arr[maxElement])

    # when size of array is even
    else:

        # find 1st maximum element
        maxElement1 = arr.index(max(arr))

        # find 2nd maximum element
        maxElement2 = arr.index(max(arr[0: maxElement1]))
        maxElement2 = arr.index(max(arr[maxElement2],
                                    max(arr[maxElement1 + 1:])))

        # swap position for median
        (arr[maxElement1],
         arr[n // 2]) = (arr[n // 2],
                         arr[maxElement1])
        (arr[maxElement2],
         arr[n // 2 - 1]) = (arr[n // 2 - 1],
                             arr[maxElement2])

    # print the resultant array
    for i in range(0, n):
        print(arr[i], end=" ")


# Driver code
if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    n = len(arr)
    printMaxMedian(arr, n)