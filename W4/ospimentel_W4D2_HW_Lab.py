# W4D2 - HW Lab
# 1/28/25
# Owen Pimentel

#----------Program prompt----------

#review for using sequenstial search and create and write data to txt file

#---IMPORTS----------------------------------
import csv



#---VAR DICONARY-----------------
#fName      list for 1st names
#lName      list for last names
#age        list for ages
#sName      list for screen names
#clan       list for House Allegiance
#email      list for emails
#depart     list for departments
#phone      list for phone exts
#phoneCount holds the phone ext
#phoneNum   used for phone ext calculations. just counts up for each employee so ext are unique
#EmpCount   number of employees

#-------Functions----------


    

#-------Main Code--------------

#create need vars and lists
fName =[]
lName = []
age = []
sName = []
clan = []
email = []
depart = []
phone = []
phoneCount = 0
phoneNum = 0
EmpCount = 0


# open file
with open("W4/got_emails.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        sName.append(rec[3])
        clan.append(rec[4])


#loop for creating emails. adds email to sName
for i in range(0, len(sName)):
    email.append(f" {rec[3]}@westeros.net")

#loop for adding departments. is created based on clan
for i in range(0, len(clan)):
    if clan[i] == "House Stark":
        depart.append(f"R&D")
    elif clan[i] == "House Targaryen":
        depart.append(f"Marketing")
    elif clan[i] == "House Tully":
        depart.append(f"HR")    
    elif clan[i] == "House Lannister":
        depart.append(f"Accounting")        
    elif clan[i] == "House Baratheon":
        depart.append(f"Sales")      
    elif clan[i] == "The Night's Watch":
        depart.append(f"Auditing") 

# loop for creating phone-ext. is created based on depart
for i in range(0, len(depart)):
    phoneNum +=1
    if depart[i] == "R&D":
        
        phoneCount = 100 + phoneNum
        phone.append(f"{phoneCount}")
        
    
    elif depart[i] == "Marketing":
        phoneCount = 200 + phoneNum
        phone.append(f"{phoneCount}")
    elif depart[i] == "HR":
        phoneCount = 300 + phoneNum
        phone.append(f"{phoneCount}")
    elif depart[i] == "Accounting":
        phoneCount = 400 + phoneNum
        phone.append(f"{phoneCount}")     
    elif depart[i] == "Sales":
        phoneCount = 500 + phoneNum
        phone.append(f"{phoneCount}")      
    elif depart[i] == "Auditing":
        phoneCount = 600 + phoneNum
        phone.append(f"{phoneCount}")         
                       
# disconnected from file. can be used later



print(f"{"FIRST":15} {"LAST":35} {"EMAIL":22} {"DEPARTMENT":20} {"EXT"}")
print("-------------------------------------------------------------------------------------")
# process loop for display

for i in range(0, len(fName)):
    print(f"{fName[i]:15} {lName[i]:30} {email[i]:30} {depart[i]:15} {phone[i]}")
    
#get number of employees.    
EmpCount = len(fName)
print(f"# of EMPLOYEES: {EmpCount}")


# Write to and create file with data
#--------------------------------------------
file = open('W4/westeros.csv', "w")

for i in range(0,len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{depart[i]},{phone[i]}\n")   
#-------------------------------------------------

    




