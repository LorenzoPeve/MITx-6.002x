
from typing import Callable


class Food(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.calories = w

    def getValue(self):
        return self.value

    def getCost(self):
        return self.calories

    def density(self):
        return self.getValue() / self.getCost()
        
    def __str__(self):
        return self.name + ': <' + str(self.value) + ', ' + \
               str(self.calories) + '>'

    def __repr__(self) -> str:
        return self.__str__()

def buildMenu(names: list[str], values: list[float], calories: list[float]):
    """
    Returns list of Foods as three-element tuples in the form 
    (name, value, calories).
    """

    menu = []
    for i in range(len(values)):
        menu.append(Food(names[i], values[i], calories[i]))
    return menu

def greedy(items: list[Food], maxCost: float, keyFunction: Callable):
    """
    Assumes items a list, maxCost >= 0, keyFunction maps elements of items to
    numbers.
    """
    itemsCopy = sorted(items, key = keyFunction, reverse = True)
    result = []
    totalValue, totalCost = 0, 0
    for item in itemsCopy:
        if (totalCost+item.getCost()) <= maxCost:
            result.append(item)
            totalCost += item.getCost()
            totalValue += item.getValue()
    return (result, totalValue)

def testGreedy(items, constraint, keyFunction):
    taken, val = greedy(items, constraint, keyFunction)
    print('Total value of items taken =', val)
    for item in taken:
        print('   ', item)

def testGreedys(foods, maxUnits):
    print('Use greedy by value to allocate', maxUnits,'calories')
    testGreedy(foods, maxUnits, Food.getValue)

    print('\nUse greedy by cost to allocate', maxUnits,'calories')
    testGreedy(foods, maxUnits, lambda x: 1/Food.getCost(x))

    print('\nUse greedy by density to allocate', maxUnits, 'calories')
    testGreedy(foods, maxUnits, Food.density)


names = ['wine', 'beer', 'pizza', 'burger', 'fries',
         'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildMenu(names, values, calories)
testGreedys(foods, 1000)