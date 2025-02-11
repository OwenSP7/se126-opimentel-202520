#w6d2 - binary search + bubble sort

#this file uses party .csv

#program prompt: build a repeatable, menu driven program to access and search for data

#------------------imports--------------
import csv

#--------------functions---------------
def display(x, foundList, records):
    '''PARAMETER
    
    x   signifier for if we are printing a single record or multiple
        when x = "x" we have one value, otherwise we jave multiple
        
        records = the length of a list we are going to proces through (number of loops/prints)'''
    
    print(f"{'CLASS':8} {'NAME':10} {'MEANING':25} {'CULTURE'}")
    print("--------------------------------------------------------------------------------")
    if x != "x":
        print(f"{class_type[x]:8} {name[x]:10} {meaning[x]:25} {culture[x]}")
        print("----------------------------------------------------------------------")
    elif foundList:
        for i in range(0, records):

            print(f"{class_type[foundList[i]]:8} {name[foundList[i]]:10} {meaning[foundList[i]]:25} {culture[found[i]]}")
    
    
    else:
        for i in range(0, records):

            print(f"{class_type[i]:8} {name[i]:10} {meaning[i]:25} {culture[i]}")

def swap(i, listName):
    temp = listName[index]
    listName[index] = name[index + 1]
    listName[index + 1] = temp
#----------main code-------------------------------------
class_type = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah","Duncan", "Justyn"]

# open file
with open("W6/party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)

    #create lists
    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#---------disconnected from file-----------------        

#display whole list to user
display("x", 0, len(class_type)) # practice with function

ans = input("would you like to enter the search program? [y/n]: ").lower()

while ans !="y" and ans !="n":
    print("INVAILD ENTRY")
    ans = input("would you like to enter the search program? [y/n]: ").lower()


#main searching loop
while ans =="y":
    print("\tSEARCHING MENU")
    print("1. SEARCH BY TYPE")
    print("2. SEARCH BY NAME")
    print("3. SEARCH BY MEANING")
    print("4. EXIT")

    search_type = input("\nHow would you like to search today? [1-4]: ")

    if search_type not in ["1", "2", "3", "4"]:
        print("INVAILD ENTRY")
        search_type = input("\nHow would you like to search today? [1-4]: ")    
    elif search_type == "1": 

    
        print(f"you have chosen to search by TYPE")

        search = input("Which type: 'dragon'or 'elf'': ").lower()

        if search not in ["dragon", "elf"]:
            #could also be: if search.title() not in class type
            print("INVAILD ENTRY")
        else:
            found = []
            for i in range(0,len(class_type)):
                if search.lower() == class_type[i].lower():
                    found.append(i)

            if not found:
                print(f"Sorry, your search could not be competed :[")
            else:
                print(f"your search for {search} is complete! details below:")
                display("x",found, len(found))

    elif search_type == "2":
        print(f"\nYou have chosen to search by NAME")





        #BUBBLE SORT----------------------------------------
        for i in range(0, len(name) - 1):#outter loop
            
            for index in range(0, len(name) - 1):#inner loop

               
               #below if statement determines the sort

              #list used is the list being sorted

               # > is for increasing order, < for decreasing

               if(name[index] > name[index + 1]):

                   

                    #if above is true, swap places!
                    swap(index,name)
 
                   #swap all other values
                    swap(index,class_type)
                    swap(index,meaning)
                    swap(index,culture)

        display("x", 0, len(name))

        #binary search
        search = input("Enter the name you are looking for: ").lower()

        min = 0
        max = len(name) - 1
        mid = int((min + max) / 2)

        while min < max and search != name[mid]:
            if search < name[mid]:
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)

        if search == name[mid]:
            display(mid,0, len(name))
        else:
            print(f"Your search for {search} came up empty")

    elif search_type == "3":
        print(f"you have chosen to search by MEAING")

        search = input("Which MEANING are you looking for: ").lower()

        found = []

        for i in range(0,len(meaning)):
            if search.lower() in meaning[i].lower():
                found.append(i)

        if not found:
            print(f"Sorry,we got no names related to what you entered")
        else:
            display("x", found, len(found))

    elif search_type == "4":
        print("you have chosen to exit")
        ans = "N"