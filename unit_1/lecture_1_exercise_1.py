"""
STATEMENT: 
As a burgler robs a house, she finds the following items:
    Dirt - Weight: 4, Value: 0
    Computer - Weight: 10, Value: 30
    Fork - Weight: 5, Value: 1
    Problem Set - Weight: 0, Value: -10

This time, she can only carry a weight of 14, and wishes to maximize the value
to weight ratio of the things she carries.

She employs three different metrics in an attempt to do this, and writes an
algorithm in Python to determine which loot to take.

The algorithm works as follows:

1. Evaluate the metric of each item. Each metric returns a numerical value 
   for each item.
2. For each item, from highest metric value to lowest, add the item if there is
   room in the bag.

"""

def metric1(item):
    """Returns value per unit of weight"""
    try:
        return item.getValue() / item.getWeight()
    except ZeroDivisionError:
        return 0

def metric2(item):
    return  -item.getWeight()

def metric3(item):
    return item.getValue()

class ItemsChooser:

    def __init__(self, items, metric):
        self.items = items
        self.metric = metric
        self.carry = 0
        self.limit = 14
        self.keeping = []

    def _sort_items(self):
        """Sorts the items based on the specified metrics"""
        self.items = sorted(
            self.items, key = lambda x: self.metric(x), reverse=True)

    def select_items(self):
        'Returns'
        self._sort_items()
        print('Sorted items: ', self.items)

        for item in self.items:

            if item.weight + self.carry <= self.limit:
                self.keeping.append((item, self.metric(item)))
                self.carry += item.weight
        return self.keeping

    def get_total_weight(self):
        return sum([item[0].weight for item in self.keeping])

    def get_total_value(self):
        return sum([item[0].value for item in self.keeping])

class ItemToSteal():

    def __init__(self, name, value, weight) -> None:
        self.name = name
        self.value = value
        self.weight = weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight


dirt = ItemToSteal('dirt', 0, 4)
computer = ItemToSteal('laptopt', 30, 10)
fork = ItemToSteal('fork', 1, 5)
pset = ItemToSteal('problem set', -10, 0)

items = [dirt, computer, fork, pset]

print('-----------------')
print('metric_1')
items = ItemsChooser([dirt, computer, fork, pset], metric1)
print(items.select_items())
print(items.get_total_weight())
print(items.get_total_value())

print('-----------------')
print('metric_2')
items = ItemsChooser([dirt, computer, fork, pset], metric2)
print(items.select_items())
print(items.get_total_weight())
print(items.get_total_value())

print('-----------------')
print('metric_3')
items = ItemsChooser([dirt, computer, fork, pset], metric3)
print(items.select_items())
print(items.get_total_weight())
print(items.get_total_value())