# W4D1 - Class Lab
# 1/27/25
# Owen Pimentel

#----------Program prompt----------

#practice connecting to a file, storing the file data into parallel lists, and creating new data for each student record based on these lists. We will then build a sequential search program which will allow us to find students in the file, and write data regarding them to a newly created file in our repository.

# ----------Variable dictionary-----------------------

#fName = First names
#lName = last names
#test1 = 1st test grades
#test2 = 2nd test grades
#test3 = 3rd test grades
#num_avg = average of all 3 tests as a number grade
#let_avg = average of all 3 tests as a letter grade


#---IMPORTS----------------------------------
import csv


#-------Functions----------
#converts number grade to letter grade

def letter(num):
    if num >= 90:
        let = "A"
    elif num >= 80:
        let ="B"
    elif num >= 70:
        let ="C"  
    elif num >= 60:
        let ="D"      
    elif num > 60:
        let ="F"
    else:
        let = "Error" 

    return let # "let"    value replaces fuction call in the main code 

#-------Main Code--------------

fName = []
lName = []
test1 = []
test2 = []
test3 = []

with open("W4/class_grades-1.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int (rec[3]))
        test3.append(int(rec[4]))
# disconnected from file. can be used later

#process the list data to calc an avg score for each student, and fins a letter grade

num_avg = [] # will hold each studnets numeric average of test scores
let_avg = [] # will hold each students letter average of test scores
class_avg = 0

for i in range(0,len(fName)):
# calculate average of current students
    a = (test1[i] + test2[i] + test3[i]) / 3

    class_avg += a

# add average to list
    num_avg.append(a)
    #can also divide in paratheisis

    l = letter(a)
    let_avg.append(l) # can also do: let_avg.append(letter(a))


class_avg = class_avg / len(num_avg)
    #process the lists to display all data to user

print(f"{'FNAME' :10} {'LNAME' :10}  {'T1' :3} {'T2' :3} {'T3' :3} {'# AVG' :6}{'L AVG'} ")

for i in range(0,len(fName)):
    print(f"{fName[i]:10} {lName[i]:10} {test1[i]:3} {test2[i]:3} {test3[i]:3} {num_avg[i]:6.2f}   {let_avg[i]}     ")
    print(f" CLASS AVERAGE: {class_avg :.2f}")
print("----------------------------------------")

print("\n\n Welocme to the Student Search Program\n\n")

answer = input("Would you like to begin searching? [y/n]: ").lower()

while answer == "y":

    print("\tSEARCH MENU OPTIONS")
    print("1. Search by Last name")
    print("2. Search by First name")
    print("3. Search by letter grade")
    print("4. exit")
    
    search_type = input("Enter your search type [1-3]: ")

    if search_type == "1":
        print ("SEARCH BY LAST NAME")

        found = -1 #invalid index number, will use to check if a student us found

        # get search item from user
        search_name = input("Enter the LAST NAME of student you want to find: ")

        #perform search
        for i in range(0, len(lName)):
            # the loop allows for the sequence part -> from the beginning to end
            if search_name.lower() == lName[i].lower():
                # if allows the search part
                found = i # make found the current index, can be used later to display

        if found != -1:
             # last name has been found.   
             print(f" Search found for {search_name}")
             print(f"{fName[found]:10} {lName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {num_avg[found]:6.2f}   {let_avg[found]}")
        else:
            print(f" search not found for {search_name}")
            print(f"check spelling and casing")
    
    
    
   

    if search_type == "2":
        print ("SEARCH BY FIRST NAME")

        found = -1 #invalid index number, will use to check if a student us found

        # get search item from user
        search_name = input("Enter the FIRST NAME of student you want to find: ")

        #perform search
        for i in range(0, len(lName)):
            # the loop allows for the sequence part -> from the beginning to end
            if search_name.lower() == fName[i].lower():
                # if allows the search part
                found = i # make found the current index, can be used later to display

        if found != -1:
             # last name has been found.   
             print(f" Search found for {search_name}")
             print(f"{fName[found]:10} {lName[found]:10} {test1[found]:3} {test2[found]:3} {test3[found]:3} {num_avg[found]:6.2f}   {let_avg[found]}")
        else:
            print(f" search not found for {search_name}")
            print(f"check spelling and casing")
    




    elif search_type == "3":
        
        print ("SEARCH BY LETTER GRADE")

        found = [] #invalid index number, will use to check if a student us found

        # get search item from user
        search_grade = input("Enter the GRADE of student you want to find: ")

        #perform search
        for i in range(0, len(lName)):
            # the loop allows for the sequence part -> from the beginning to end
            if search_grade.upper() == let_avg[i]:
                # if allows the search part
                found.append(i) # make found the current index, can be used later to display

        if not found:
             print(f" search not found for {search_name}")
             print(f"check spelling and casing")
            
        else:
             # last name has been found.   
             for i in range(0, len(found)):
                print(f" Search found for {search_grade}")
                print(f"{fName[found[i]]:10} {lName[found[i]]:10} {test1[found[i]]:3} {test2[found[i]]:3} {test3[found[i]]:3} {num_avg[found[i]]:6.2f}   {let_avg[found[i]]}")
    
    elif search_type == "4":
        print("EXITING")
        answer = "n"







    if search_type == "1" or search_type == "2":
        answer = input("Would you like to begin searching again? [y/n]: ").lower()
          
    