# Exercise 1


# Generate all combinations of N items
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

      Yields a tuple, (bag1, bag2), where each bag is represented as 
      a list of which item(s) are in each bag.
    """

class Item(object):
    def __init__(self, n, v, w):
        self.name = n
        self.value = float(v)
        self.weight = float(w)
    
    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return '<' + self.name + ', ' + str(self.value) + ', '\
                     + str(self.weight) + '>'

    def __repr__(self) -> str:
        return (f'(name = {self.name}, value = {self.value},'
            f'weight = {self.weight})')

def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]


# items = buildItems()
combos = powerSet([1,2,3])

count = 0
for _ in range(20):
    count+=1
    print(next(combos))
    print(count)

# print(next(combos))
# print(next(combos))
# print(next(combos))
# print(next(combos))
# # count = 0
# print(next(combos))
# a = next(combos)
# print(type(a))
# print(a)
# while next(combos):
#     count += 1

# print(count)

def simple_gen():

    yield 

