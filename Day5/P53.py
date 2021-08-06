######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import sys, os
sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


def main():
	s=input()
	freq=dict()
	#please make use of the above dictionary 'freq' to store the result
	#complete the rest of the code













	#the following lines are provided to print the output in the appropriate format
	result=', '.join('{}:{}'.format(k,v) for k,v in freq.items())
	print(result)


#dont delete the following part
if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########