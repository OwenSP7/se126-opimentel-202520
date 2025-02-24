# W8D1 - Lab 6
# 2/24/25
# Owen Pimentel


#-----PROGRAM PROMPT-------------------

#a Python program using lists to assign passengers seats in an airplane


#----VARIABLES-------------------------------------------

#seatCounter - used to end program when all seats are filled



#-----IMPORTS----------------------------------


#------FUNCTIONS------------------------------

def display():
    

    # this handles the seat display
    for i in range(len(seatA)):
        print(f" Row {i + 1}  {seatA[i]} {seatB[i]}      {seatC[i]} {seatD[i]}")
       

#------MAIN CODE------------------------------

#create lists
seatA = ["A" ,"A" ,"A" ,"A" ,"A" ,"A" ,"A"]
seatB = ["B" ,"B" ,"B" ,"B" ,"B" ,"B" ,"B"]
seatC = ["C" ,"C" ,"C" ,"C" ,"C", "C" ,"C"]
seatD = ["D" ,"D" ,"D" ,"D" ,"D" ,"D" ,"D"]


seatCounter = 0



print("Welcome!")
print("Here is the seating layout of the plane")



# main loop for runtime. program wont end untill user leaves loop
ans = "y"
while ans == "y":
    
    display()

    #ends program if all seats have been filled
    if seatCounter != 28:
        
        # get data from user
        chosenRow = int(input(" What Row would like to be seated at?[1-7]: "))
        chosenSeat = input(" What seat would like? [A,B,C,D]: ").upper()

        

        # chained if statements. takes chosen seat and row and appends them with an X to show them as filled
        if chosenSeat.upper() == "A":
            if seatA[chosenRow - 1] != "X":
                seatA[chosenRow - 1] = "X"
                seatCounter += 1
                display()
                ans = input(" Would you like to reserve another seat?[y/n]: ").lower()
            else:
                print(f"Sorry, looks like {chosenRow}{chosenSeat} is alreay taken")
        elif chosenSeat.upper() == "B":
            if seatB[chosenRow - 1] != "X":
                seatB[chosenRow - 1] = "X"
                seatCounter += 1
                display()
                ans = input(" Would you like to reserve another seat?[y/n]: ").lower()
            else:
                print(f"Sorry, looks like {chosenRow}{chosenSeat} is alreay taken")
        elif chosenSeat.upper() == "C":
            if seatC[chosenRow - 1] != "X":
                seatC[chosenRow - 1] = "X"
                seatCounter += 1
                display()
                ans = input(" Would you like to reserve another seat?[y/n]: ").lower()
            else:
                print(f"Sorry, looks like {chosenRow}{chosenSeat} is alreay taken")
        elif chosenSeat.upper() == "D":
            if seatD[chosenRow - 1] != "X":
                seatD[chosenRow - 1] = "X"
                seatCounter += 1
                display()
                ans = input(" Would you like to reserve another seat?[y/n]: ").lower()
            else:
                print(f"Sorry, looks like {chosenRow}{chosenSeat} is alreay taken")               
        else:
            # error trap
            print("INVALID ENTRY")
    else:
        # ends program because all seats are filled
        print("all seats have been filled")
        
        ans = "n"

        
        