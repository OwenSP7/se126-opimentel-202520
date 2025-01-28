# W4D2 - HW Lab
# 1/28/25
# Owen Pimentel

#----------Program prompt----------

#review for using sequenstial search and create and write data to txt file

#---IMPORTS----------------------------------
import csv


#-------Functions----------


    

#-------Main Code--------------

fName =[]
lName = []
age = []
sName =[]
clan = []


with open("W4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        clan.append(rec[3])

        
# disconnected from file. can be used later

# process loop for display

#print(f"{"DRAGONS":15} {"RIDER":30} {"#":3} {"COLOR1":8} {"COLOR2"}")
print("-------------------------------------------------------------------------------------")

#for i in range(0, len(dragons)):
#    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")




