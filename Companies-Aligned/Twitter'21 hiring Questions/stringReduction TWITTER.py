# def stringReduction(string):
#     return len(string)-len(set(string))



MAX_CHAR=[26]
def stringReduction(s):
    n=len(s)

    if(n>MAX_CHAR[0]):
        return -1
    distinct=0
    count=[0]*MAX_CHAR[0]

    for letters in s:
        if(count[ord(letters)-ord('a')])==0:
            distinct+=1
        count[(ord(letters)-ord('a'))]+=1

    return (n-distinct)


s='aebaecedabbee'
print(stringReduction(s))