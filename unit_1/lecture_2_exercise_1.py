# Exercise 1

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
    combi_bag_1 = powerSet(items)
    
    while True:

        try:
            c1 = next(combi_bag_1)
            combi_bag_2 = powerSet(list(set(items).difference(set(c1))))
            while True:
                try:
                    c2 = next(combi_bag_2)
                    yield (c1, c2)
                except StopIteration:
                    break
        except StopIteration:
                break


def buildItems():
    return [Item(n,v,w) for n,v,w in (('clock', 175, 10),
                                      ('painting', 90, 9),
                                      ('radio', 20, 4),
                                      ('vase', 50, 2),
                                      ('book', 10, 1),
                                      ('computer', 200, 20))]

# Testing powerSet Generator
gen = powerSet([1,2,3])
combinations = []
while True:
    try:
        combinations.append(next(gen))
    except StopIteration:
        break

assert combinations == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]


# Testing powerSet Generator
gen = yieldAllCombos([1,2,3])
combinations = []
while True:
    try:
        combinations.append(next(gen))
    except StopIteration:
        break

print(combinations)
print(len(combinations))



def yieldAllCombos_bitwise(items):
    """
    Generates all combinations of N items into two bags, whereby each item is
    in one or zero bags.

    Yields a tuple, (bag1, bag2), where each bag is represented as a list of
    which item(s) are in each bag.
    """
    N = len(items)
    # Enumerate the 3**N possible combinations   
    for i in range(3**N):
        bag1 = []
        bag2 = []
        for j in range(N):
            if (i // (3 ** j)) % 3 == 1:
                bag1.append(items[j])
            elif (i // (3 ** j)) % 3 == 2:
                bag2.append(items[j])
        yield (bag1, bag2)