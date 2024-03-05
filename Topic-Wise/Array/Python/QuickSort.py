def Partition(arr,low,high):

    pivot=arr[low]

    for i in range(low+1,high):
        for j in range(high,low):
            while (i < j):
                while (arr[i] <= pivot):
                    i = i + 1
                while (arr[j] > pivot):
                    j = j - 1
                if (arr[i] > pivot and arr[j] < pivot):
                    arr[i], arr[j] = arr[j], arr[i]
                    i = i + 1
                    j = j - 1
            pivot = arr[j]
            return j



def QuickSort(arr,low,high):

    if (low<high):
        j=Partition(arr,low,high)
        QuickSort(arr,low,j-1)
        QuickSort(arr,j+1,high)


arr=[17,14,31,13,2]
QuickSort(arr,0,4)
print(arr)

