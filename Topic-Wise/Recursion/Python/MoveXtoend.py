newString= ''
def Movextoend(s, idx, count):
    global newString
    if(idx==len(s)):
        newString += 'x' * count
        print(newString)
        return
    if(s[idx] == 'x'):
        count+=1
    else:
        newString+=s[idx]
    Movextoend(s,idx+1, count)

if __name__ == '__main__':
    Movextoend("ababdcxxbdbsxbsbsbx",0, 0);
