#to find fib(n) using dynamic proramming

def fibFast(n,memo={}):
    if n==0 or n==1:
        memo[n]=n
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n]=fibFast(n-1,memo)+fibFast(n-2,memo)
        return memo[n]

print(fibFast(150))
