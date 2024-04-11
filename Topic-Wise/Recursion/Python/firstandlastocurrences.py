first =-1
last = -1

def occurrences(s, idx, c):
    global first, last

    if(idx == len(s)):
        print(first)
        print(last)
        return

    if s[idx]==c:
        if first==-1:
            first = idx
        else:
            last = idx
    occurrences(s, idx+1, c)

if __name__ == '__main__':
    occurrences("abcaaefaghad", 0, 'a')