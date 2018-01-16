# Uses python3
def evalt(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    n=int(len(dataset)/2)+1
    ops=[]
    digits=[]
    for i in range(len(dataset)):
        if i%2==1:
            ops.append(dataset[i])
        else:
            digits.append(int(dataset[i]))
    M={}
    m={}
    # for i in range(n):
    #     l=[0]*n
    #     M.append(l)
    #     m.append(l)

    for i in range(1,n+1):
        M[(i,i)]=digits[i-1]
        m[(i,i)]=digits[i-1]

    for s in range(1,n):
        for i in range(1,n-s+1):
            j=i+s
            m[(i,j)],M[(i,j)]=MinMax(i,j,M,m,ops)

    return M[(1,n)]


def MinMax(i,j,M,m,ops):
    minimum=10**15
    maximum=-10**15
    for k in range(i,j):
        a=evalt(M[(i,k)],M[(k+1,j)],ops[k-1])
        b=evalt(M[(i,k)],m[(k+1,j)],ops[k-1])
        c=evalt(m[(i,k)],M[(k+1,j)],ops[k-1])
        d=evalt(m[(i,k)],m[(k+1,j)],ops[k-1])
        minimum=min(minimum,a,b,c,d)
        maximum=max(maximum,a,b,c,d)

    return minimum,maximum



if __name__ == "__main__":
    print(get_maximum_value(input()))
