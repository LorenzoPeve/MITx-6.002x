# Write a function, stdDevOfLengths(L) that takes in a list of strings, L, and
# outputs the standard deviation of the lengths of the strings. 
# Return float('NaN') if L is empty.

def stdDevOfLengths(L: list[str]):
    """Returns the standard deviation of the lengths of the strings. """

    if len(L) == 0:
        return float('NaN')

    str_lengths = []
    for s in L:
        str_lengths.append(len(s))

    avg = sum(str_lengths) / len(str_lengths)

    var = 0 
    for s in str_lengths:
        var += (s-avg)**2

    return (var / len(str_lengths))**0.5


output = stdDevOfLengths(['apples', 'oranges', 'kiwis', 'pineapples'])
assert abs(output - 1.8708) < 0.0001


## Testing empirical rule of Normal Distribution
import scipy.integrate
import random
import pylab

def gaussian(x, mu, sigma):
    factor1 = (1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2 = pylab.e**-(((x-mu)**2)/(2*sigma**2))
    return factor1*factor2
    
def checkEmpirical(numTrials):
  for t in range(numTrials):
     mu = random.randint(-10, 10)
     sigma = random.randint(1, 10)
     print('For mu =', mu, 'and sigma =', sigma)
     for numStd in (1, 1.96, 3):
        area = scipy.integrate.quad(gaussian,
                                    mu-numStd*sigma,
                                    mu+numStd*sigma,
                                    (mu, sigma))[0]
        print('  Fraction within', numStd, 'std =', round(area, 4))
 
checkEmpirical(3)