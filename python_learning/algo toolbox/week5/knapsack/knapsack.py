# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    T={}
    l=len(w)
    for j in range(0,l+1):
        T[(0,j)]=0
    for i in range(0,W+1):
        T[(i,0)]=0

    for i in range(1,W+1):
        for j in range(1,l+1):
            if w[j-1]>i:
                T[(i,j)]=T[(i,j-1)]
            else:
                T[(i,j)]=max(T[(i-w[j-1],j-1)]+w[j-1],T[(i,j-1)])

    return T[(W,l)]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))

