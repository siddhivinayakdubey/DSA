s="FORGEEKSSKEEGFOR"
print(list(s))

def longestsubstring(s):
    main=list(s)
    max=0


    i=0
    j=i+1
    while (j<len(main)):
        if(main[i]==main[j]):
            arr1=main[:j]
            arr2=main[j:]


            print(arr1)
            print(arr2)

            x=len(arr1)-1
            y=0
            count = 0
            while(arr1[x]==arr2[y]):
                count+=1
                x-=1
                y+=1
            if count>max:
                max=count

            i+=1
            j+=1

        else:
            i+=1
            j+=1

    return max*2

print(longestsubstring(s))
