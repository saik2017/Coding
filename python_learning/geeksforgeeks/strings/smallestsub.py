import sys
import random

def merge(A,B):
    m=len(A)
    n=len(B)
    i,j,L=0,0,[]
    while i<m and j<n:
        if A[i]<=B[j]:
            L.append(A[i])
            i+=1
        else:
            L.append(B[j])
            j+=1
    if i==m:
        L+=B[j:]
    else:
        L+=A[i:]

    return L

def test_merge(m,n):
    A,B=[],[]
    for i in range(m):
        A.append(random.randint(0,m))
    A.sort()
    print(A)
    for j in range(n):
        B.append(random.randint(0,n))
    B.sort()
    print(B)
    print(merge(A,B))

#test_merge(5,6)

if __name__ == '__main__':
    input=sys.stdin.read()
    data=list(map(int,input.split()))
    t=data[0]
    data=data[1:]
    for i in range(t):
        m,n,k=data[0],data[1],data[2]
        A=data[3:3+m]
        B=data[3+m:3+m+n]
        print(merge(A,B)[k-1])
        data=data[3+m+n:]








