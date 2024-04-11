def allsubseq(s, idx, newString):
    if(idx==len(s)):
        print(newString)
        return
    currchar=s[idx]

    allsubseq(s,idx+1,newString+currchar);
    allsubseq(s,idx+1,newString);

if __name__ == '__main__':
    allsubseq("abc",0,"")