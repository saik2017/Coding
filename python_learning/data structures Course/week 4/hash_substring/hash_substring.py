# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def PolyHash(S,p,x):
    ans = 0
    for c in reversed(S):
        ans = (ans * x + ord(c)) % p
    return ans

def PreComputeHashes(text,l1,p,x):
    l2=len(text)
    H=[0]*(l2-l1+1)
    S=text[l2-l1:]
    H[l2-l1]=PolyHash(S,p,x)
    y=1
    for i in range(l1):
        y=(y*x)%p
    for i in range(l2-l1-1,-1,-1):
        H[i]=(x*H[i+1]+ord(text[i])-y*ord(text[i+l1]))%p
    return H



def get_occurrences(pattern, text):
    p=100123456789
    x=263
    result=[]
    pHash=PolyHash(pattern,p,x)
    H=PreComputeHashes(text,len(pattern),p,x)
    for i in range(len(text)-len(pattern)+1):
        if pHash!=H[i]:
            continue
        if text[i:i+len(pattern)]==pattern:
            result.append(i)
    return result




if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

