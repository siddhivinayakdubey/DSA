def recursiveprint(x):
    if x != 0:
        recursiveprint(x-1)
        print(x)

if __name__ == '__main__':
    recursiveprint(5)