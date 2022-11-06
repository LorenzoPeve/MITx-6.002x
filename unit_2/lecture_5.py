import random
import matplotlib.pyplot as plt
import seaborn as sns

###############################################################################
# Stochastic Processes 

# Exercises 2 and 3
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''  
    return random.sample(range(0, 101, 2), 1)[0]

def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    return 16

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number
    between 9 and 21
    '''
    outcomes = list(range(10, 21, 2))
    return random.sample(outcomes, 1)[0]

# Exercise 4
# 4.1 Are the following two distributions equivalent? ANS: Yes
    # The random.random() distribution is uniform, so both dist1 and dist2 are
    # a uniform distribution over [-1.0, 1.0).

def dist1():
    return random.random() * 2 - 1

def dist2():
    if random.random() > 0.5:
        return random.random()
    else:
        return random.random() - 1 

def compare_dists(f1, f2, **kwargs):
    """Compares two distributions using a sample of 10,000 points graphically.
    """

    d1 = [f1() for _ in range(10_000)]
    d2 = [f2() for _ in range(10_000)]    

    fig, ax = plt.subplots(1, 2, figsize = (10, 5))

    ax1 = sns.histplot(data = None, x = d1, ax = ax[0],  **kwargs)
    ax1.set_title('f_1')

    ax2 = sns.histplot( data = None, x = d2, ax = ax[1],  **kwargs)
    ax2.set_title('f_2')
    plt.show()

compare_dists(dist1, dist2, binwidth = 0.1)

# 4.2 Are the following two distributions equivalent? ANS: Yes
    # The random.random() distribution is uniform, and so is the
    # random.randrange() distribution, so both dist3 and dist4 are a discrete
    # uniform distribution over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

def dist3():
    return int(random.random() * 10)

def dist4():
    return random.randrange(0, 10)

compare_dists(dist3, dist4, bins = list(range(0, 11)))

# 4.3 Are the following two distributions equivalent? ANS: No

    # Thus dist5 is a discrete U(0,9) over [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # dist6 is a discrete U(0,10) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10].

def dist5():
    return int(random.random() * 10)

def dist6():
    return random.randint(0, 10) # Includes 10

compare_dists(dist5, dist6, bins = list(range(0, 11)))


###############################################################################
# Probabilities