#Owen Pimentel
#W1D2 Lab Demo: SE116 Review
#1-7-2025 [W1D2]

#PROGRAM PROMPT: This is a temperature conversion program, it allows a user to enter as many Fahrenheit temps as they'd like and then shows the Celsius conversoion for each. It also counts the number of temps and determines the average of all temps entered. 

#VARIABLE DICTIONARY
#temp_count     the total number of all temps entered
#temp_total     the sum total of all temps entered
#avg_temp       the avg temp entered (avg_temp = temp_total / temp_count)
#tempF          the temp in Fahrenheit, entered by the user
#tempC          the temp in Celsius (tempC = (tempF - 32) * (5 / 9))
#answer         loop control; value determines if loop repeats, entered by the user

#--------IMPORTS----------------------------------------------

#--------FUNCTIONS--------------------------------------------
def again(): #<-----Function header
    '''This Function asks a user if they'd like to enter another temp. checks the respose or validity, and then returns a valid response back to the main program'''

    #loop control! allowing a way back in or out of the loop based on the value of answer
    ans = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    #while loop trap - ensure user provides valid value before moving on
    while ans != "y" and ans != "n":
        print("! invaild entry !")

        return ans 
    
def converter(f):
    '''this fucntion is passsed a tempF value (the f parameter), converts to celsius and returns '''

    c = (f - 32) * (5/9)

    return c



#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
temp_count = 0
temp_total = 0

answer = "y"

#start of loop - will be based on answer, and user can change value at end of loop
while (answer == "y" or answer == "Y") and temp_total >= 0:

    tempF = float(input("\t\tEnter temperature in Fahrenheit: "))

    #necessary calculations
    #tempC = (tempF - 32) * (5 / 9)
    tempC = converter(tempF)
    #math processes needed later for average calculation

    #tracks amount of temps entered by user
    temp_count = temp_count + 1
    temp_total += tempF

    #display data to user
    print(f"\n\t\tTEMP# {temp_count}\tTEMP {tempF:.1f}F = TEMP {tempC:.1f}C\n")

    #loop control! allowing a way back in or out of the loop based on the value of answer
    #answer = input("\t\tWould you like to enter another temperature? [y/n]: ").lower()

    answer = again()

#out of loop

#average calculation and conversion
avg_tempF = temp_total / temp_count 

avg_tempC = converter(avg_tempF)


#final displays
print("\n\t\tHere is your final session information: ")
print("\t\tTOTAL TEMPS ENTERED: {0}".format(temp_count))
print("\t\tAVGERAGE TEMP {0:.1f}F  |  {1:.1f}C".format(avg_tempF, avg_tempC))

print("\n\n\t\tThank you for using the program. Goodbye.\n\n")



