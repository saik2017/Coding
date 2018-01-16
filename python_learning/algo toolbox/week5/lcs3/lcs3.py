#Uses python3

import sys

def lcs3(a, b, c):
    m,n,r=len(a),len(b),len(c)
    D={}
    for j in range(n+1):
        for k in range(r+1):
            D[(0,j,k)]=0
    for i in range(m+1):
        for k in range(r+1):
            D[(i,0,k)]=0
    for i in range(m+1):
        for j in range(n+1):
            D[(i,j,0)]=0


    for i in range(1,m+1):
        for j in range(1,n+1):
            for k in range(1,r+1):
                deletion1=D[(i-1,j,k)]
                deletion2=D[(i-1,j-1,k)]
                deletion3=D[(i-1,j,k-1)]
                insertion1=D[(i,j-1,k)]
                insertion2=D[(i,j,k-1)]
                insertion3=D[(i,j-1,k-1)]
                match=D[(i-1,j-1,k-1)]+1
                mismatch=D[(i-1,j-1,k-1)]
                if a[i-1]==b[j-1]==c[k-1]:
                    D[(i,j,k)]=max(deletion1,deletion2,deletion3,insertion1,insertion2,insertion3,match)
                else:
                    D[(i,j,k)]=max(deletion1,deletion2,deletion3,insertion1,insertion2,insertion3,mismatch)

    return D[(m,n,r)]











if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))

def lcs2(A,B):
    D={}
    m=len(A)
    n=len(B)
    for i in range(m+1):
        D[(i,0)]=0
    for j in range(n+1):
        D[(0,j)]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            insertion=D[(i,j-1)]
            deletion=D[(i-1,j)]
            mismatch=D[(i-1,j-1)]
            match=D[(i-1,j-1)]+1
            if A[i-1]==B[j-1]:
                D[(i,j)]=max(insertion,deletion,match)
            else:
                D[(i,j)]=max(insertion,deletion,mismatch)

    return D[(m,n)]



#print(lcs3([8,3,2,1,7],[8,2,1,3,8,10,7],[6,8,3,1,4,7]))
