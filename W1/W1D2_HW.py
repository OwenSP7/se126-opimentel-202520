#Owen Pimentel
#W1D2 HW Lab: SE116 Review
#1-7-2025 [W1D2]

#PROGRAM PROMPT: This is a prgram that checks if a meeting meets fire safety standards.

#VARIABLE DICTIONARY
#meetName       the name of the meet
#maxPeople      the max amount of people allowed in the room
#peopleThere    how many peole will be at the meeting
#finalCount     the diffrence between people there and max people allowed
#answer         loop control; value determines if loop repeats, entered by the user

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
def decision(response): 
    

    # this function traps user if entry in invaild. prompts them to re-enter if it was invalid. return entry

    
    while response != "y" and response != "n":
        print("! invaild entry !")

        response = input("\t\tWould you like to continue the program?? [y/n]: ")

        
    return response     
    
def diffrence(people, max_cap):
    
    #this fucntion get the diffrence between people attending and the max allowed to attend the meeting and then returns this value
    
    
    diff = max_cap - people
    
    return diff
    


#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables

answer = "y"

#start of loop - will be based on answer, and user can change value at end of loop
while (answer == "y" or answer == "Y"):
    print("Welcome!")

    # collect needed data from user
    meetName = input("What is the name of the meeting?: ")
    maxPeople = float(input("What is the Max amount of people allowed in the room?: "))
    peopleThere = float(input("How many people are attending the meeting?: "))

    # call the difference function, send data so it can run
    finalCount = diffrence(maxPeople, peopleThere)


    # display final data. message displayed depends on if they meet fire standards or not
    if finalCount < 0:
        
        finalCount = abs(finalCount)

        print(f"\n\tYour all Good! you can add {finalCount} people to the meeting and still be within fire safety standards!  ")

    elif finalCount > 0:
        
        print(f"\n\tYou have too many people attending! you have remove {finalCount} people from the meeting to be within fire safety standards!  ")
    else:
        print(f"\n\tYour all Good! you meet fire safety standards! just don't add anyone else!  ")




    
    # prompts user to rerun program or end
    answer = input("\t\tWould you like to continue the program?? [y/n]: ")
    decision(answer)





#final-final displays
print("\n\n\t\tThank you for using the program. Goodbye.\n\n")



