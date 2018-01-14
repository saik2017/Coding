# Uses python3
import sys

def lcm(a, b):
    g=(gcd(a,b))
    #print(g)
    c=int((b/gcd(a,b)))
    #print(c)
    #print(int(a*c))
    return (a*c)


def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    #print(lcm_naive(226553150,1023473145))
    print(lcm(a, b))

# we try to reduce the size of numbers in order to avoid overflow error.
# so to calculate ab/gcd(a,b) we do a*(b/gcd(a,b))
