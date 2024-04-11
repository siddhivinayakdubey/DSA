Chars = set()
result =""
def removeduplicates(s, idx):
    # global result
    # if(idx == len(s)):
    #     print(result)
    #     return
    # if(s[idx] not in Chars):
    #     Chars.add(s[idx])
    #     result+=s[idx]
    # removeduplicates(s,idx+1)

    #OR
    string = set(s)
    str = ''
    for chars in string:
        str+=chars;
    print(str)

if __name__ == '__main__':
    removeduplicates("abbcdddebdceba", 0);
