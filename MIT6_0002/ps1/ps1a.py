###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: vaisko
# Collaborators:N/A
# Time: 23:48:59 10/10/2023 in Cologne

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here

    dict = {}
    file = open(filename)
    
    for line in file:
        data = line.strip().split(',')
        if data[0] in dict:
            raise KeyError('Cow not unique')
        dict.update({data[0]:int(data[1])})
    file.close()
    return dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    return_list = []
    cowlist = [*cows.keys()]
    
    while cowlist:
        remaining = limit
        sublist = []

        while remaining >= 0:
            topcow = ''
            for cow in cowlist:
                if cows.get(cow) <= remaining:
                    if not topcow:
                        topcow = cow
                    elif cows.get(cow) > cows.get(topcow):
                        topcow = cow

            if not topcow:
                break

            sublist.append(topcow)
            remaining -= cows.get(topcow)
            cowlist.remove(topcow)
            
        return_list.append(sublist)

    return return_list

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    return_list = []
    cowlist = [*cows.keys()]
    min_trips = len(cowlist)

    for partition in get_partitions(cowlist):
        
        is_valid = True

        for sublist in partition:
            sublist_weight = 0
            for element in sublist:
                sublist_weight += cows.get(element)
            if sublist_weight > limit:
                is_valid = False
                break
        
        if len(partition)<min_trips and is_valid:
            min_trips = len(partition)
            return_list.clear()
            return_list = partition

    return return_list
    
                


    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """

    cows = load_cows("MIT6_0002/ps1/ps1_cow_data.txt")
    
    print(f'For list of {len(cows)} cows:\n\n')

    startg = time.time()
    greedy = greedy_cow_transport(cows,10)
    endg = time.time()
    
    startb = time.time()
    brute = brute_force_cow_transport(cows,10)
    endb = time.time()

    print(f'Greedy algorithm\n----\ntrips: {len(greedy)}\nruntime: {endg-startg}s\n\n')
    print(f'Brute force algorithm\n----\ntrips: {len(brute)}\nruntime: {endb-startb}s\n\n')

    return



if __name__ == '__main__':

    compare_cow_transport_algorithms()

