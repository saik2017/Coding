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


def greedyMaxVal(toConsider,avail):
    if toConsider==[] or avail==0:
        return (0,())
    elif toConsider[0].getCost()>avail:
        return greedyMaxVal(toConsider[1:],avail)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=greedyMaxVal(toConsider[1:],avail-nextItem.getCost())
        withVal+=nextItem.getValue()
        withoutVal,withoutToTake=greedyMaxVal(toConsider[1:],avail)
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    return result

def greedyMaxValFast(toConsider,avail,memo={}):
    if (len(toConsider),avail) in memo:
        result=memo[(len(toConsider),avail)]
    elif toConsider==[] or avail==0:
        result=(0,())
    elif toConsider[0].getCost()>avail:
        result=greedyMaxValFast(toConsider[1:],avail,memo)
    else:
        nextItem=toConsider[0]
        withVal,withToTake=greedyMaxValFast(toConsider[1:],avail-nextItem.getCost(),memo)
        withVal+=nextItem.getValue()
        withoutVal,withoutToTake=greedyMaxValFast(toConsider[1:],avail,memo)
        if withVal>withoutVal:
            result=(withVal,withToTake+(nextItem,))
        else:
            result=(withoutVal,withoutToTake)
    memo[len(toConsider),avail]=result
    return result



names=['wine','beer','pizza','burger','fries','cola','apple','donut']
values=[89,90,95,100,90,79,50,10]
calories=[123,154,258,354,365,150,95,195]
items=BuildMenu(names,values,calories)
print(greedyMaxValFast(items,1000))