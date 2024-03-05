def closestNumbers(arr):
    # Write your code here
    n=len(arr)
    arr.sort()
    Chhota = arr[1] - arr[0]
    final = [arr[0], arr[1]]
    for i in range(1, len(arr) - 1):
        if arr[i + 1]-arr[i] < Chhota:
            final = []
            final.append(arr[i])
            final.append(arr[i + 1])
            Chhota = abs(arr[i + 1] - arr[i])
        elif arr[i + 1]-arr[i] == Chhota:
            final.append(arr[i])
            final.append(arr[i + 1])
    return final
