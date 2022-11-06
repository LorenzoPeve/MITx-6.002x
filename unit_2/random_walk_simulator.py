import random
from models import Field, Location, Drunk, UsualDrunk, ColdDrunk

def walk(f: Field, d: Drunk, numSteps: int) -> float:
    """
    Moves d numSteps times, and returns the distance between
    the final location and the location at the start of the walk.
    """
    start = f.getLoc(d)
    for _ in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))
    
def simWalks(numSteps: int, numTrials: int, dClass: Drunk) -> list:
    """
    Simulates numTrials walks of numSteps steps each.
    Returns a list of the final distances for each trial
    """

    Homer = dClass()
    origin = Location(0, 0)
    distances = []
    for _ in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(round(walk(f, Homer, numSteps), 1))
    return distances

def drunkTest(walkLengths: list[int], numTrials: int, dClass: Drunk):
    """
    For each number of steps in walkLengths, runs simWalks with
    numTrials walks and prints results
    """
    
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', round(sum(distances)/len(distances), 4))
        print(' Max =', max(distances), 'Min =', min(distances))

random.seed(0)
drunkTest((10, 1000, 1000, 10000), 100, UsualDrunk)