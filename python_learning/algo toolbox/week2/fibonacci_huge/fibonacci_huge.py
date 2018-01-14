# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n<=1:
        return n
    previous = 0
    current  = 1
    period=1
    rem_list=[0,1]

    while True:
        previous, current = current%m, (previous + current)%m
        if previous==0 and current==1:
            rem_list.pop()
            break
        else:
            period+=1
            rem_list.append(current%m)

    #print(period)
    #print(rem_list)

    return rem_list[n%period]


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
