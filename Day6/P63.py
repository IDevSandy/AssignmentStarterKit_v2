######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########

def read_int():
    try:
        x = input()
        x = int(x)
    except Exception as e: 
        print('Bad Input {}.'.format(x))
        print('Try Again.')
        x = read_int()
        return x
    else:
        return x


## Add code to read __VendingItems__.csv


def main():
    ## Code to read user inputs
    ## Enforce the constraints using Exception Handling
    pass

    ## Act once the inputs are OK.





if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########