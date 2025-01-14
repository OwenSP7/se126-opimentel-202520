#Owen Pimentel
#W2D1 class Lab
#1-13-2025 [W2D1]

#PROGRAM PROMPT: 

#VARIABLE DICTIONARY
#total_rec      total number of rooms
#rooms_over     number of rooms that have too many people
#name           names of rooms
#max            the max capacity of room 
#ppl            number of poeple in room
#remaining      number of people that need to be removed from room

#--------IMPORTS----------------------------------------------
import csv

#--------FUNCTIONS--------------------------------------------

def difference(people, max_cap):

    diff = max_cap - people
    return diff

#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
total_rec = 0
rooms_over = 0

print(f"{'NAME':20}    {'MAX':7} {'PPL':5}   {'OVER'}") # field header
print("-----------------------------------------------------------")


#-----conected to file---------------
with open("W2/classLab2.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for rec in file:
        #below code occurs for every row in the file

        #print (record)

        name = rec[0]
        max = int(rec[1])
        ppl = int(rec[2])

        #call the diff func
        remaining = difference(ppl,max)

        if remaining < 0:
            rooms_over += 1
    
            print(f"{name:20}  {max:5}   {ppl:5}   {abs(remaining):5}")

        total_rec +=1

        



#final displays

print(f"total rooms on file: {total_rec}")

print(f"Rooms over capacity: {rooms_over}")

#count and display over cap rooms.

   

