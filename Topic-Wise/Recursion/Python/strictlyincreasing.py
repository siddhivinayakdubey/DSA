def strictcheck(arr, i):
    if(i==len(arr)-1):
        print("Strictly increasing")
        return True
    if arr[i] < arr[i+1]:
        return strictcheck(arr, i+1)
    else:
        print("Not a strictly increasing one")
        return False

if __name__ == '__main__':
    arr=[1,2,3,4,5]
    strictcheck(arr,0)