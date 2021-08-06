######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


# Complete the following function which takes 2 input from user the initial velocity and angle of the projectile
# and plots the trajectory of projectile and prints 3 values:
# 1 - time of flight
# 2 - total horizontal distance covered
# 3 - Peak height achieved
def main():
    # Take the user input

    # You have to calculate the following values
    t = 0.0  # The time of flight
    d = 0.0  # Distance covered by the projectile
    y = 0.0  # Peak Height achieved by the projectile

    # Output the calculated values NOTE: DO NOT change the format of the output. Changing this may cause the tests to fail
    print('Time of Flight = {}'.format(round(t, 2)))
    print('Distance Covered = {}'.format(round(d, 2)))
    print('Peak Height = {}'.format(round(y, 2)))


# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    # Call the main function
    main()
