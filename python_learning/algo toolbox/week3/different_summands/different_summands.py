# Uses python3
import sys

def optimal_summands(n):
    summands=[]
    l=1
    if n<=2:
        return [n]
    while True:
        if n>2*l:
            summands.append(l)
            n-=l
            l+=1
        else:
            summands.append(n)
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x,end=' ')

