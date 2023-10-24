###########################
# 6.0002 Problem Set 1b: Space Change
# Name: vaisko
# Collaborators: vaisko.com
# Time: 0.002s
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """

    if len(egg_weights) == 1:
        return target_weight//egg_weights[0]

    else:
        return target_weight//egg_weights[-1] + dp_make_weight(egg_weights[:-1], target_weight - (target_weight//egg_weights[-1])*egg_weights[-1])
            

# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = ", egg_weights)
    print("n = ", n)
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print("-"*40)

    egg_weights = tuple(range(3, 500))
    n = 250
    print("Egg weights = ", egg_weights)
    print("n = ", n)
    print("Output:", dp_make_weight(egg_weights, n))
    print("-"*40)

    egg_weights = (7,8)
    n = 456
    print("Egg weights = ", egg_weights)
    print("n = ", n)
    print("Output:", dp_make_weight(egg_weights, n))
    print("-"*40)
