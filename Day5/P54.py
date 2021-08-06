######## IMMUTABLE CODE SECTION BEGIN ########

# helper library functions
import numpy as np
from scipy import linalg
import sys, os

sys.path.insert(0, "..")
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))


######## IMMUTABLE CODE SECTION END ########

########## USER CODE SECTION BEGIN #########


temp_records=dict()
final_records=dict()
total=[20,100,100,50]
weight=[0.15,0.4,0.2,0.25]


def add_student():
	#complete the function
    #read user inputs(roll number) and add them to temp_records, till the input is '-1'
    #terminate the function on seeing '-1'
    pass



def read_marks():
    #complete the function
    #read the input(roll number), if it does not exist in temp_records then print ""ERROR: Student roll number does not exist"" 
    #else read 4 inputs, which corresponds to the marks of quiz, exam, assignment, project, check their validity. If any of them are invalid print the appropriate error message, based on yesterday's GPA program
    pass



#On seeing user input 3: call the below two functions sequentially, i.e compute_gpa first then assign_grade.
#If roll number exists, compute the gpa and grade and update it in temp_records
#else print "ERROR: Student roll number marks information unavailable"
def compute_gpa(roll):
    #complete the function
    pass



def assign_grade(roll):
    #complete the function
    pass

def generate_records():
	#complete the function
    #use this to merge temp_records and final_records as specified in the question
    pass


def display_records():
    #complete the function
    #use this to take an input roll number, display the values of the final_records dictionaries corresponding to that roll number(key) if it exists. Else print ""ERROR: Student roll number does not exist""  
	pass



# This is required to ensure that we can import your solve function without activating other parts of code
def main():
    #write your code here
    #try to write the logic for the menu-driven part here and call the above functions based on the user input command
    pass



if __name__ == "__main__":
    # Call the main function
    main()

######### USER CODE SECTION END #########