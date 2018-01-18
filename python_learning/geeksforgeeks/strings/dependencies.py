import sys

def maxGold(M):
    m=len(M)
    n=len(M[0])
    D={}
    for i in range(m):
        D[(i,0)]=M[i][0]


    for j in range(1,n):
        for i in range(m):
            if i==0:
                right=D[(i,j-1)]+M[i][j]
                if m>1:
                    right_up=D[(i+1,j-1)]+M[i][j]
                    D[(i,j)]=max(right,right_up)
                else:
                    D[(i,j)]=right
            elif i==m-1:
                right_down=D[(i-1,j-1)]+M[i][j]
                right=D[(i,j-1)]+M[i][j]
                D[(i,j)]=max(right,right_down)
            else:
                right_down = D[(i-1, j - 1)] + M[i][j]
                right = D[(i, j - 1)] + M[i][j]
                right_up = D[(i + 1, j - 1)] + M[i][j]
                D[(i,j)]=max(right,right_down,right_up)
    maximum=-1
    for i in range(0,m):
        if D[(i,n-1)]>maximum:
            maximum=D[(i,n-1)]
    return maximum

#print(maxGold([[1,3,1,5],[2,2,4,1],[5,0,2,3],[0,6,1,2]]))
#print(maxGold([[1,2,3,4]]))


if __name__=="__main__":
    input=sys.stdin.read()
    data=list(map(int,input.split()))
    t=data[0]
    data=data[1:]
    for i in range(t):
        m=data[0]
        n=data[1]
        data=data[2:]
        L=[]
        for j in range(m):
           L.append(data[0:n])
           data=data[n:]
        print(maxGold(L))

























