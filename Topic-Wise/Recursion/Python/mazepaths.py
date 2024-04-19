def mazepaths(m,n,i,j,path):

    if(i==m-1 and j==n-1):
        print(path)
        return

    if(i<m-1):
        mazepaths(m,n,i+1,j,path+'R')
    if (j<n-1):
        mazepaths(m,n,i,j+1,path+'D')

if __name__ == '__main__':
    mazepaths(3,3,0,0,"")