######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import pandas as pd
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

# Implement following solve function which takes as user input path to the iris.csv file and
# prints column wise means for 3 cases as follows:
# 1) having missing values filled using highest frequency element of each column
# 2) having missing values filled using class wise mean of each column
# 3) hvaing missgin values filled using class wise median of each column
def main():
    # Take path to csv file from user and read the file in a pandas data structure



    # Fill the missing values in the pandas data structure and create 3 new data structures, one for each case
    iris_df_highest_freq = None
    iris_df_classwise_mean = None
    iris_df_classwise_median = None



    # print column wise mean. NOTE: DO NOT change the format of the output. Else it may cause the tests to fail
    print("Column wise means:")
    print(iris_df_highest_freq.mean())
    print(iris_df_classwise_mean.mean())
    print(iris_df_classwise_median.mean())



if __name__ == "__main__":
    # Call the main function
    main()