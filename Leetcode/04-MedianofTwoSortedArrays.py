
def solution(nums1,nums2):
    arr=[]
    i=0
    j=0
    if(len(nums1)==0 and len(nums2)==0):
        return 0

    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            arr.append(nums1[i])
            i+=1
        else:
            arr.append(nums2[j])
            j+=1

    if i<len(nums1):
        arr+=nums1[i:]

    elif j<len(nums2):
        arr+=nums2[j:]

    print(arr)
    x=len(arr)
    if x%2==0:
        y=x//2
        final=(arr[y]+arr[y-1])/2
        return final
    else:
        return arr[x//2]


nums1=[2]
nums2=[1]
print(solution(nums1,nums2))
