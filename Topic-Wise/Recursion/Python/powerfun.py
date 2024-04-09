def powerfun(x,n):
    if x == 0:
        return 0
    if n == 0:
        return 1
    p_mn1= powerfun(x,n-1);
    p = x * p_mn1
    
    return p

if __name__ == '__main__':
    print(powerfun(5,3))
