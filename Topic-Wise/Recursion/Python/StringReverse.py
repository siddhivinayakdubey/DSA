def reverse(s, idx):
    if(idx==0):
        print(s[idx])
        return
    print(s[idx], end="")
    reverse(s, idx-1)

if __name__ == '__main__':
    reverse("hello",4)