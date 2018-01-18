import sys
from collections import deque


def firstNonRepeat(A):
    S=set()
    singles=[]
    L=[]
    for letter in A:
        if letter not in S:
            S.add(letter)
            singles.append(letter)
        else:
            if letter in singles:
                singles.remove(letter)
        if singles==[]:
            L.append(-1)
        else:
            L.append(singles[0])
    return L

#print(firstNonRepeat('aac'))

if __name__=="__main__":
    input=sys.stdin.read()
    data=list(map(str,input.split()))
    t=int(data[0])
    data=data[1:]
    for i in range(t):
        n=int(data[0])
        A=data[1:n+1]
        L=firstNonRepeat(A)
        for i in L:
            print(i,end=" ")
        print(" ")
        data=data[n+1:]















