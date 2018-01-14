# Uses python3
import sys
class item(object):
    def __init__(self,value,weight):
        self.value=value
        self.weight=weight
        self.density=value/weight
    def getValue(self):
        return self.value
    def getWeight(self):
        return self.weight
    def getDensity(self):
        return self.density




def get_optimal_value(capacity, weights, values):
    value = 0.0
    # write your code here
    items_list=[]
    # we first create a list of elements of type item
    for i in range(len(values)):
        items_list.append(item(values[i],weights[i]))
    #we sort the list by using a class method as key and reverse to get decreasing order
    items_list_sorted=sorted(items_list,key=item.getDensity,reverse=True)
    for thing in items_list_sorted:
        if capacity<=0.0:
            break
        if thing.getWeight()<=capacity:
            value+=thing.getValue()
            capacity-=thing.getWeight()
        else:
            value+=capacity*(thing.getDensity())
            capacity=0.0

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
