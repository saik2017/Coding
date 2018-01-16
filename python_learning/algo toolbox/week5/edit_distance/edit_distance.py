# Uses python3
def edit_distance(s, t):
    """

    :param s:string1
    :param t: string2
    :return: The edit distance and also prints the alignment
    """

    #write your code here
    n=len(s)
    m=len(t)
    D=[]
    A=''
    B=''
    for i in range(n+1):
        l=[0]*(m+1)
        D.append(l)
    for j in range(m+1):
        D[0][j]=j
    for i in range(n+1):
        D[i][0]=i

    for j in range(1,m+1):
        for i in range(1,n+1):
            insertion=D[i][j-1]+1
            deletion=D[i-1][j]+1
            match=D[i-1][j-1]
            mismatch=D[i-1][j-1]+1
            if s[i-1]==t[j-1]:
                D[i][j]=min(insertion,deletion,match)
            else:
                D[i][j]=min(insertion,deletion,mismatch)
    # we now output the alignment
    i,j=n,m
    while i!=0 or j!=0:
        if  D[i][j]==D[i-1][j]+1:
            A=s[i-1]+A
            B='_'+B
            i-=1
        elif  D[i][j]==D[i][j-1]+1:
            A='_'+A
            B=t[j-1]+B
            j-=1
        else:
            A=s[i-1]+A
            B=t[j-1]+B
            i-=1
            j-=1

    print(A)
    print(B)

    return D[n][m]




if __name__ == "__main__":
    print(edit_distance(input(), input()))
