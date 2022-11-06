import random

# Exercise 2
    # 1. Is the following code deterministic or stochastic? Ans: stochastic
    # This code sample returns a list of 7s. The length of the list is
    # determined by a stochastic variable (the first call to randint).

mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
print(mylist)

# 2. Which of the following alterations (Code Sample A or Code Sample B) would
# result in a deterministic process?
    # Code Sample A will always return [7]. Code Sample B will always return
    # [1,9,7,8,10,9]. 
    # Therefore both of these versions of the original code are deterministic.

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)
   
    
# Code Sample B
mylist = []

random.seed(0)
for i in range(random.randint(1, 10)):
    if random.randint(1, 10) > 3:
        number = random.randint(1, 10)
        mylist.append(number)
    print(mylist)