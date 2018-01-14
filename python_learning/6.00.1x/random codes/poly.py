import random


def standard(a,prime):
    """
    converts the tuple form of a(x) into a standard form under mod prime 
    with leading  coefficient not equal to zero
    """
    b=list(a)
    l=len(b)
    if l==0:
        return (0,)
    r=[]
    for i in range(l-1,-1,-1):
        if b[i]%prime!=0:
            break
    for j in range(i+1):
        temp=b[j]%prime
        r.append(temp)
        
        
    r=tuple(r)
    
    return r
            


def multiply(p,q,prime):
    """
    P and q are polynomials in form of tuples
    returns product of p(x) and q(x) as a tuple 
    """
    p=standard(p,prime)
    q=standard(q,prime)
    if len(p)==1:
        l=len(q)
    elif len(q)==1:
        l=len(p)
    else:        
        l=(len(p)-1)+(len(q)-1)+1
    r=[]
    for i in range(l):
        temp=0
        for j in range(i+1):
            if j>=len(p) or i-j>=len(q):
                temp+=0
            else:
                temp+=p[j]*q[i-j]
        r.append(temp%prime)        
    r=tuple(r)
    op=standard(r,prime)
    return op        
            
def add(p,q,prime):
    """
    P and q are polynomials in form of tuples
    returns the sum of p(x) and q(x) as a tuple 
    """
    p=standard(p,prime)
    q=standard(q,prime)
    
    l=max(len(p),len(q))
    r=[]
    for i in range(l):
        if i>=len(p):
            temp=q[i]
        elif i>=len(q):
            temp=p[i]
        else:
            temp=p[i]+q[i]
        r.append(temp%prime)
    r=tuple(r)
    op=standard(r,prime)
    return op           

def subtract(p,q,prime):
    """
    P and q are polynomials in form of tuples
    returns the difference of p(x) and q(x) as a tuple 
    """
    p=standard(p,prime)
    q=standard(q,prime)
    
    l=max(len(p),len(q))
    r=[]
    for i in range(l):
        if i>=len(p):
            temp=-q[i]
        elif i>=len(q):
            temp=p[i]
        else:
            temp=p[i]-q[i]
        r.append(temp%prime)
    r=tuple(r)
    op=standard(r,prime)

    return op

def inverse_num(a,b):
    """
    returns the inverse of b under field a
    """
    p=a
    x2=1
    x1=0
    y2=0
    y1=1
    while b>0:
        q=a/b
        r=a-(b*q)
        x=x2-(q*x1)
        y=y2-(q*y1)
        a=b
        b=r
        x2=x1
        x1=x
        y2=y1
        y1=y
    y=y2
    y=y%p    
    return y

def divide(a,b,prime):
    """
    divides a(x) by b(x)  to give a  list quotient and remainder under mod prime

    """
    a=standard(a,prime)
    b=standard(b,prime)
    
    k=len(a)
    l=len(b)
    r=[]
    q=range(k-l+1)
    Q=[]
    R=[]
    if k<l:
        q=0
        r=a
        return (q,r)
    t=inverse_num(prime,b[l-1])
    for i in range(k):
        temp=a[i]
        r.append(temp)
    for i in range(k-l,-1,-1):
        temp=t*r[i+l-1]
        q[i]=temp
        for j in range(l):
            r[i+j]-=q[i]*b[j]
    for i in range(k-l+1):
        temp=q[i]%prime
        Q.append(temp)
        
    for i in range(l-1):
        temp=r[i]%prime
        R.append(temp)
    Q=standard(tuple(Q),prime)
    R=standard(tuple(R),prime)    
    return (Q,R)        
        
                   
def zero(a,prime):
    a=standard(a,prime)
    l=len(a)
    for i in range(l):
        if a[i]%prime!=0:
            return False
    return True        
                  
def inverse(g,h,prime):
    """
    computes the inverse of h(x) wrt to g(x) under mod prime
    ie g(x)s(x)+h(x)t(x)=d(x)(gcd)
    """
    g=standard(g,prime)
    h=standard(h,prime)
    
    s1=(0,)
    s2=(1,)
    t1=(1,)
    t2=(0,)
    s=()
    t=()
    d=()
    while zero(h,prime)==False:
        dummy=divide(g,h,prime)
        (q,r)=(dummy[0],dummy[1])
        temp=multiply(q,s1,prime)
        s=subtract(s2,temp,prime)
        temp=multiply(q,t1,prime)
        t=subtract(t2,temp,prime)
        (g,h)=(h,r)
        (s2,s1,t2,t1)=(s1,s,t1,t)
       
        
    (d,s,t)=(g,s2,t2)   
    return (d,s,t)
    
def num_binary(n):
    a=n
    l=[]
    if a==0:
        return 0
    while a!=0:
        l.insert(0,a%2)
        a/=2
    return l    

def exponent(g,f,n,prime):
    b=num_binary(n)
    b=b[::-1]
    l=len(b)
    s=(1,)
    if n==0:
        return s
    G=g
    if b[0]==1:
        s=g
    for i in range(1,l):
        temp1=multiply(G,G,prime)  
        temp2=divide(temp1,f,prime)
        G=temp2[1]
        if b[i]==1:
            temp3=multiply(G,s,prime)
            temp4=divide(temp3,f,prime)
            s=temp4[1]
    return s        
        
                    
def is_irreducible(f,prime):
    if len(f)==1:
        return False
    u=(0,1)
    m=len(f)-1
    for i in range(1,(m/2)+1):
        temp1=exponent(u,f,prime,prime)
        temp2=subtract(temp1,(0,1),prime)
        temp3=inverse(f,temp2,prime)
        d=temp3[0]
        if d!=(1,):
            return False
            
    return True    
    
        
                            
                                                         

def generate_irreducible(prime,m):
    l=[]
    state=True
    while state==True:
        for i in range(m):
            x=random.randint(0,prime-1)
            l.append(x)
        l.append(1)
        r=tuple(l)
        if is_irreducible(r,prime)==True:
            state=False
        
    return r
        
                     
                                                                