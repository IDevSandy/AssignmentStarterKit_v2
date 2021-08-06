# helper library functions
import pandas as pd
import numpy as np
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

########## USER CODE SECTION BEGIN #########

# Feel free to define any other methods or global variables if you feel the need
def main():
    # Take the path to the marks.csv file as input
    marks_file = input()

    #  Read the file in a pandas dataframe


    # Create a second dataframe to store the results. It can initially have the same content as marks.csv
    result_df = None

    # Calculate the GPA and grades for each student and update the result_df dataframe.

    # Save the results in a result.csv file in the same location as that of marks.csv
    # NOTE: DO NOT Change the path where the result.csv is saved since the we need to read this result.csv file
    # while running the tests
    out_path = os.path.split(marks_file)[0] + os.sep + "result.csv"
    result_df.to_csv(out_path)


# This is required to ensure that we can import your solve function without activating other parts of code
if __name__ == "__main__":
    main()
    
########## USER CODE SECTION END #########
