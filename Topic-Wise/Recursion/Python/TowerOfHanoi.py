def TOH(n, S, H, D):
    if n == 1:
        print("Transferring Disk "+str(n)+" from "+S+" to "+D)
        return
    TOH(n-1, S, D, H)
    print("Transferring Disk "+str(n)+" from "+S+" to "+D)
    TOH(n-1, H, S, D)

if __name__ == '__main__':
    TOH(4, "Source", "Helper", "Destination");