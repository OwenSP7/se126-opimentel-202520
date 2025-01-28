#Owen Pimentel
#W3D1 HW Lab
#1-27-2025 [W3D1]

#PROGRAM PROMPT: 
#  program that will analyze potential voters. The program generates the following totals:

#Number of individuals not eligible to register.
#Number of individuals who are old enough to vote but have not registered.
#Number of individuals who are eligible to vote but did not vote.
#Number of individuals who did vote.
#Number of records processed.

#VARIABLE DICTIONARY
# id            list for voter ID numbers
# age           list for age of voters
# regi          list to see if voters are registered or not 
# voted         list to see if voters voted
#totalYoung     total number of people too young to vote
#totalNoRegi    total number of people who didnt register
#totalRegi      number of people who registered but did not voter
#totalVoted     number of people who voted
#totalRec       number of voters processed

#--------IMPORTS----------------------------------------------
import csv

#--------FUNCTIONS--------------------------------------------




#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables
id = []
age = []
regi = []
voted = []

totalYoung = 0
totalNoRegi = 0
totalRegi = 0
totalVoted = 0
totalRec = 0


print("-------------------------------------------------------------------")


#-----conected to file---------------
with open("W3/voters_202040.csv") as csvfile:

    file = csv.reader(csvfile)
    

    for rec in file:
        #below code occurs for every row in the file

        #fill lists with data from file. age has to be cast as a int for use later
        id.append(rec[0])
        age.append(int(rec[1]))
        regi.append(rec[2])
        voted.append(rec[3])

        totalRec += 1
    #-------disconnected from file---------

    # indexes for each list. conditonals are used to determine what totals are added too.
    #-----------------------------------------------------------------------
    
    # checks each voters age to see if they are under 18
    for i in range(0, len(age)):
        
        if age[i] < 18:
            totalYoung += 1

    # checks to see if each voter is registered or not and if they voted
    for i in range(0, len(regi)):
        
        if regi[i] == "Y" and voted[i] == "N":
            totalRegi += 1
        elif regi[i] == "N" and age[i] < 18:
            totalNoRegi += 1

    # checks to see of voters voted
    for i in range(0, len(voted)):
        
        if voted[i] == "Y":
            totalVoted += 1      

#------------------------------------------------------------  
               

# final display

print(f" Number of people who are too young to register:     {totalYoung}")
print(f" Number of people who who can register but arent:    {totalNoRegi}")
print(f" Number of people who are registered but didnt vote: {totalRegi}")
print(f" Number of people who voted:                         {totalVoted}")

print(f" Number of voter records processed:                  {totalRec}")

        
        
           


        
        

        
        
            

       
        



    

        







   

