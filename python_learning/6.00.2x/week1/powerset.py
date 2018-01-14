from itertools import chain,combinations

def genPowerSet(items):
    for z in chain.from_iterable(combinations(items, r) for r in range(len(items) + 1)):
        yield (list(z))




#python3
def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 2 == 1:
                combo.append(items[j])
        yield combo



def yieldAllCombos(items):
    """
        Generates all combinations of N items into two bags, whereby each
        item is in one or zero bags.

        Yields a tuple, (bag1, bag2), where each bag is represented as a list
        of which item(s) are in each bag.
    """
    # Your code here
    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3**N):
        combo = ([],[])
        for j in range(N):
            if (int(i/(3**j))%3) == 1:
                combo[0].append(items[j])
            elif (int(i/(3**j))%3)==2:
                combo[1].append(items[j])
        yield combo
