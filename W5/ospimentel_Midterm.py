# W5D1 - Midterm
# 2/4/25
# Owen Pimentel
# Choice 1


#-------IMPORTS----------------------------------
import csv



#-------PROGRAM PROMPT------------------------------

#Gets employees First and Last Name, email, department and phone extension from a csv file. The program also assigns each employee a unique office number between 100-200. The program has a sequential search that allows user to search for email or department.

#---VAR DICONARY-----------------
#fName          list for first names
#lName          list for last names
#email          list for emails
#depart         list for departments
#phone          list for phone exts
#officeNum      list for office number
#officeCount    used for office number calculations. just counts up for each employee so numbers are unique
#recCount       number of records on file

#-------Functions----------


    

#-------Main Code--------------

#create need vars and lists
fName =[]
lName = []
email = []
depart = []
phone = []
officeNum = []
officeCount = 0
recCount = 0


# open file
with open("W5\westeros.csv") as csvfile:
    file = csv.reader(csvfile)

    #create lists
    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        depart.append(rec[3])
        phone.append(rec[4])
        





# loop for creating office-num. 
for i in range(0, len(fName)):
   
   if len(officeNum) < 1:
        officeNum.append(100)
   else:
        officeCount +=1

        officeNum.append(100 + officeCount)
    
# disconnected from file. can be used later



print(f"{"FIRST":15} {"LAST":35} {"EMAIL":30} {"DEPARTMENT":20} {"EXT":3} {"OFFICE #"}")
print("------------------------------------------------------------------------------------------------------------------------")

# process loop for display
for i in range(0, len(fName)):
    print(f"{fName[i]:15} {lName[i]:30} {email[i]:30} {depart[i]:25} {phone[i]:5} {officeNum[i]}")
    
#get number of recs on file and print to user
recCount = len(fName)
print(f"# of RECS on file: {recCount}")






# sequential search begins here

answer ="y"

while answer == "y":
    print(" Westeros Services Directory Search")
    print("------------------------------------")
    print("\tSEARCH MENU OPTIONS")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT")
    
    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
        print ("SEARCH BY EMAIL")

        found = -1 #invalid index number, will use to check if a student us found

        # get search item from user
        search_name = input("Enter the EMAIL of employee you want to find: ")

        #perform search
        for i in range(0, len(email)):
            # the loop allows for the sequence part -> from the beginning to end
            if search_name.lower() == email[i].lower():
                # if allows the search part
                found = i # make found the current index, can be used later to display

        if found != -1:
             # last name has been found.   
            print(f" Search found for {search_name}")

            print(f"{"FIRST":15} {"LAST":35} {"EMAIL":30} {"DEPARTMENT":20} {"EXT":3} {"OFFICE #"}")
            print("------------------------------------------------------------------------------------------------------------------------")  

            print(f"{fName[found]:15} {lName[found]:30} {email[found]:30} {depart[found]:25} {phone[found]:5} {officeNum[found]}")
        else:
            print(f"\nSEARCH NOT FOUND FOR {search_name}")
            print(f"CHECK SPELLING!\n")
    
    
    
   

    if search_type == "2":
        print ("SEARCH BY DEPARTMENT")

        found = [] #invalid index number, will use to check if a student us found

        # get search item from user
        search_name = input("Enter the DEPARTMENT of employee you want to find: ")

        print(f"{"FIRST":15} {"LAST":35} {"EMAIL":30} {"DEPARTMENT":20} {"EXT":3} {"OFFICE #"}")
        print("------------------------------------------------------------------------------------------------------------------------")  

        #perform search
        for i in range(0, len(depart)):
            # the loop allows for the sequence part -> from the beginning to end
            if search_name.lower() == depart[i].lower():
                # if allows the search part
                found.append(i) # make found the current index, can be used later to display

        if not found:
              print(f"\nSEARCH NOT FOUND FOR {search_name}")
              print(f"CHECK SPELLING!\n")
        else:
            for i in range(0, len(found)):
                
                print(f"{fName[found[i]]:15} {lName[found[i]]:35} {email[found[i]]:30} {depart[found[i]]:20} {phone[found[i]]:5} {officeNum[found[i]]}")
    

    elif search_type == "3":
        print("EXITING")
        answer = "n"
    



# Write to and create file with data
#--------------------------------------------
file = open('midterm_choice1.csv', "w")

for i in range(0,len(fName)):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{depart[i]},{phone[i]},{officeNum[i]}\n")   
#-------------------------------------------------



    #if search_type == "1" or search_type == "2":
    #    answer = input("Would you like to search again? [y/n]")