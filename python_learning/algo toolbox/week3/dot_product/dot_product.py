#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    if len(a)==len(b)==1:
        return (a[0]*b[0])
    else:
        a_max=max(a)
        b_max=max(b)
        a.remove(a_max)
        b.remove(b_max)
        return (a_max*b_max)+max_dot_product(a,b)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

