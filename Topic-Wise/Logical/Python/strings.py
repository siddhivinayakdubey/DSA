# a = "Hello"
# b=""
# n=len(a)
# i=0
# j=n-1
# while(i<j):
#     temp=a[i]
#     a[i]=a[j]
#     a[j]=temp
#
#     i+=1
#     j-=1
# print(a)
s="hellyyseo"
str=""
for i in s:
    str=i+str
print(str)

res={}
for char in s:
    res[char]=s.count(char)

print(res)

for item in res:
    if(res[item]>1):
        print(item)
