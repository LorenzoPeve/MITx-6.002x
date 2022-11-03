###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time
import sys
import os

os.chdir(os.path.abspath(os.path.join(os.path.abspath(__file__), '..')))

# Notes from Problem Statement:
# Goal: optimize transport
# Details:
    # Weights are only integers

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename: str) -> dict[str, int]:
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as 
    values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows: dict[str, int], limit=10) -> list[list]:
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. 
    The returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow
        that will fit to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows
    """

    def _greedy(cows: tuple):        
        """
        This helper function recursively adds cows to trips and replaces the
        transported cows with False boolean values to progress towards base
        case.
        """

        if any(cows) == 0:
            return

        trip = []
        cum_weight = 0
        for i, cow_i in enumerate(cows):

            # Check before adding
            if cow_i is not False and (cum_weight + cow_i[1]) <= limit: 
                trip.append(cow_i[0])
                cum_weight += cow_i[-1]
                cows[i] = False        

        trips.append(trip)
        _greedy(cows_sorted)


    cows_sorted = (
        sorted(cows.items(), key=lambda item: item[1], reverse = True))
    trips = []
    _greedy(cows_sorted)

    return trips



# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force. The brute force algorithm should follow the following
    method:

    1. Enumerate all possible ways that the cows can be divided into separate
        trips
    2. Select the allocation that minimizes the number of trips without making
        any trip that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run 
    your greedy_cow_transport and brute_force_cow_transport functions here. 
    Use the default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass



cows = load_cows("ps1_cow_data.txt")



# # print(brute_force_cow_transport(cows, limit))

cows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
expected =[['Jesse', 'Maybel'], ['Maggie', 'Callie']]
assert expected == greedy_cow_transport(cows, 10)