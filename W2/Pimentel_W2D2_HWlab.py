#Owen Pimentel
#W2D1 HW Lab
#1-14-2025 [W2D1]

#PROGRAM PROMPT: displays computer information from cls file to user. Converts some data to hbe compatiable with python

#VARIABLE DICTIONARY
#type           Desktop or Laptop
#brand          brand of pc
#cpu            cpu of pc
#ram            name of pc
#oneDisk        storage of 1st hdd
#hhd            number of hdds
#twoDisk        storage of 2nd hdd. if present
#os             operating system of pc
#year           year of os or when the pc was made, idk

#--------IMPORTS----------------------------------------------
import csv

#--------FUNCTIONS--------------------------------------------




#--------MAIN EXECUTING CODE----------------------------------

#initializing needed variables


print(f"{'TYPE':8}  {'BRAND':7}  {'CPU':3}   {'RAM':3}   {'1ST DISK':7} {'HDD':4}{'2ND DISK':6}    {'OS':3}   {'YEAR':3}")   
print("-------------------------------------------------------------------")


#-----conected to file---------------
with open("W2/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for rec in file:
        #below code occurs for every row in the file

        # this if statement prevents code from crashing due to differing coloum amounts.
        if rec [6] == "001TB" or rec [6] == "500GB":
            type = rec[0]
            brand = rec[1]
            cpu = rec[2]
            ram = rec[3]
            oneDisk = rec[4]
            hdd = rec [5]
            twoDisk = rec [6]
            os = rec [7]
            year = rec [8]
        else:
            type = rec[0]
            brand = rec[1]
            cpu = rec[2]
            ram = rec[3]
            oneDisk = rec[4]
            hdd = rec [5]
            os = rec [6]
            year = rec [7]
            # set value of twoDisk since it doesnt have a value from cls file.
            twoDisk = ""

        # Changes D and L from cls file to
        if type == "D":
           type = "Desktop"
       
        elif type == "L":
            type = "Laptop"

        if brand == "DL": 
            brand = "Dell"

        elif brand == "GW":
            brand = "Gateway"

        print(f"{type:10}  {brand:7} {cpu:3}   {ram:3}   {oneDisk:6}   {hdd:3}   {twoDisk:6}   {os:3}    {year:3}")        




    

        


#final displays


#count and display over cap rooms.

   

