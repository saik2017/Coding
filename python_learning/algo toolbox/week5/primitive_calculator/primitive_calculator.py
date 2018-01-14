# Uses python3
import sys
import time


def optimal_sequence(n):
    count=[0,0,1,1]
    sequence=[[0],[1],[1,2],[1,3]]
    for m in range(4,n+1):
        l=[]
        t=2*m
        if m%2==0:
            t1=count[int(m/2)]+1
            if t1<t:
                l=sequence[int(m/2)]+[m]
                t=t1
        if m%3==0:
            t2=count[int(m/3)]+1
            if t2<t:
                l=sequence[int(m/3)]+[m]
                t=t2
        t3=count[m-1]+1
        if t3<t:
            l=sequence[m-1]+[m]
            t=t3
        count.append(t)
        sequence.append(l)
    return sequence[n]







input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# start=time.time()
# l=optimal_sequence(10**6)
# print(len(l))
# end=time.time()
# print(end-start)
