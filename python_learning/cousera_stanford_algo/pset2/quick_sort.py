def quick_sort(A,n):
    if n==1:
        return A
    if n==0:
        return []    
       
    else:
        p=A[0]
        A=partition(A,0,n-1,p)
        i=A.index(p)
        left=A[:i+1]
        right=A[i+1:]
        l1=[]
        l2=[]
        if len(left)>=1:
            l1=quick_sort(left,len(left))
        if len(right)>=1:    
            l2=quick_sort(right,len(right))
            
        A=l1.extend(l2)
                    
        return A    
    
    



def partition(A,l,r,p):
    """
    partitions the arary A between the indices l and r around the pivot p
    
    """
    i=A.index(p)
    temp=A[l]
    A[l]=p
    A[i]=temp
    i=l+1
    
    for j in range(l+1,r+1):
        if A[j]<p:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
            i+=1
            
    A[l]=A[i-1]
    A[i-1]=p
   
    return A
    