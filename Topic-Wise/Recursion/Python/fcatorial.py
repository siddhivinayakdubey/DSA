def factorial(x):
    if x==1 or x==0:
        return 1
    fact_nm1=factorial(x-1)
    fact= fact_nm1 * x
    return fact

if __name__ == '__main__':
    print(factorial(5))