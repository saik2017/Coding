#python3
class item(object):
    """
    creates an instance of class object item
    """
    def __init__(self,name,value,weight):
        self.name=name
        self.value=value
        self.weight=weight

    def __str__(self):
        return self.name+' :<'+str(self.value)+','+str(self.weight)+'>'

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getCost(self):
        return self.weight

    def getDensity(self):
        return (self.value/self.weight)

def BuildMenu(names,values,weights):
    """
    creates and return a menu based on the input
    :param names: is a list of names of items
    :param values: is a list of values of items corresponding to the names
    :param weights:  is a list of weights of the items corresponding to the names
    :return: returns a list of objects items
    """
    menu=[]
    for i in range(len(names)):
        menu.append(item(names[i],values[i],weights[i]))
    return menu

def greedy(items,maxcost,keyFunction):
    result,total_value,total_cost=[],0,0
    items_copy=sorted(items,key=keyFunction,reverse=True)
    for i,thing in enumerate(items_copy):
        if total_cost+thing.getCost()<=maxcost:
            result.append(thing)
            total_value+=thing.getValue()
            total_cost+=thing.getCost()
    return (result,total_value,total_cost)

def testGreedy(items,constraint,keyFunction):
    taken,value,cost=greedy(items,constraint,keyFunction)
    print('Total value  of items taken is :'+str(value))
    print('Total cost of items taken is :'+str(cost))
    for i in taken:
        print(' ',i)


def testGreedys(maxvalue):
    print('Use greedy by value to allocate',maxvalue,'calories')
    testGreedy(items,maxvalue,item.getValue)
    print('\n use greedy by cost to allocate',maxvalue,'calories')
    testGreedy(items,maxvalue,lambda x: 1/item.getCost(x))
    print('\n use greedy by density to allocate',maxvalue,'calories')
    testGreedy(items,maxvalue,item.getDensity)


names=['wine','beer','pizza','burger','fries','cola','apple','donut']
values=[89,90,95,100,90,79,50,10]
calories=[123,154,258,354,365,150,95,195]
items=BuildMenu(names,values,calories)
testGreedys(1000)

