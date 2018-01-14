# Uses python3
def calc_fib(n):
    a=1
    b=1
    if n==0:
        return 0
    if n==1 or n==2:
        return 1
    for i in range(n-2):
        temp=a+b
        a=b
        b=temp
    return b


n = int(input())
print(calc_fib(n))
