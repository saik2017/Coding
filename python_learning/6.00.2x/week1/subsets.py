def subsets(l):
    if len(l)==0:
        return [[]]
    sub=[]
    first=l[0]
    rest=l[1:]
    for s in subsets(rest):
        sub.append(s)
        sub.append([first]+s)
    return sub

l='evil'

def combinations(word):
    if len(word)==1:
        return word
    comb=[]
    for i,first in enumerate(word):
        rest=word[:i]+word[i+1:]
        for s in combinations(rest):
            if (first+s) not in comb:
                comb.append(first+s)
            if (s+first) not in comb:
                comb.append(s+first)
    return comb

print(subsets(l))
print(combinations(l))


