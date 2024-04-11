seq=set()
def uniquesub(s,idx,newString):
    if(idx==len(s)):
        if newString not in seq:
            seq.add(newString)
            print(newString)
        return

    currchar=s[idx]

    uniquesub(s,idx+1,newString+currchar)
    uniquesub(s,idx+1,newString)


if __name__ == '__main__':
    uniquesub("aaa", 0,"")