# Uses python3
import sys

def get_change(m):
    count=0
    if m==0:
        return m
    count+=int(m/10)
    m=m%10
    count+=int(m/5)
    m=m%5
    count+=m
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
