# W6D1 - Lab 5
# 2/10/25
# Owen Pimentel


#-----PROGRAM PROMPT-------------------

#a personal library search system using the file book_list.csv. allows user to choose from menu to search for books using different parameters(ex: title authors, etc...)


#----VARIABLES-------------------------------------------

#library_num    - stores unique library numbers
#titles         - stores tiles
#authors        - stores authors
#genres         - stores genres
#pages          - stores pages
#status         - stores the status of the books
#search_type    - stores users menu choice

#-------IMPORTS----------------------------------
import csv

#-------------------Functions------------

# used for bubble sort. reorders values based on the sort
def swap(i, listName):
    temp = listName[index]
    listName[index] = library_num[index + 1]
    listName[index + 1] = temp

#---------Main code--------------------------------

# int vars
library_num = []
titles = []
authors = []
genres = []
pages = []
status =[]

# open file
with open("W6/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    #create lists
    for rec in file:
        library_num.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])
        status.append(rec[5])
# close file


ans = "y"

# main loop. cant end program until this loop is exited by user choosing exit
while ans == "y":


    print("\tSEARCHING MENU")
    print("1. SHOW ALL TITLES")
    print("2. SEARCH BY TITLES")
    print("3. SEARCH BY AUTHOR")
    print("4. SEARCH BY GENRE")
    print("5. SEARCH BY LIBRARY NUMBER")
    print("6. SHOW ALL AVAILABLE")
    print("7. SHOW ALL ON LOAN")
    print("8. EXIT")

    search_type = input("\nHow would you like to search today? [1-8]: ")

    #user error trap
    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("INVAILD ENTRY")
        search_type = input("\nHow would you like to search today? [1-8]: ")
    
    elif  search_type == "1":
        print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
        print("-------------------------------------------------------------------------------------")

        for i in range(0, len(library_num)):
            print(f"{library_num[i]:5} {titles[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5} {status[i]}")    
    
    elif  search_type == "2":  

        # SEQUENTIAL SEARCH: allow user to search for a title


       
        found = [] 
        search = input("Which title are you looking for: ").lower()

        for i in range(0,len(titles)):
           
            if search in titles[i].lower():
                found.append(i)

        if not found:
            print(f" Search not found for {search} was not found")
        else:
            print(f"Search found for {search}")
           
            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
        for i in range(0, len(found)):
            print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5} {status[found[i]]}") 

    elif  search_type == "3":  

        # SEQUENTIAL SEARCH: allow user to search for a author


       
        found = [] 
        search = input("Which author are you looking for: ").lower()

        for i in range(0,len(authors)):
            
            if search in authors[i].lower():
                found.append(i)

        if not found:
            print(f" Search not found for {search} was not found")
        else:
            print(f"Search found for {search}")
           
            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
        for i in range(0, len(found)):
            print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5} {status[found[i]]}") 

    elif  search_type == "4":  

        # SEQUENTIAL SEARCH: allow user to search for a genre


        found = [] 
        search = input("Which genre are you looking for: ").lower()

        for i in range(0,len(genres)):
           
            if search in genres[i].lower():
                found.append(i)

        if not found:
            print(f" Search not found for {search} was not found")
        else:
            print(f"Search found for {search}")
           
            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
        for i in range(0, len(found)):
            print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5} {status[found[i]]}") 

    elif search_type == "5":

        #BUBBLE SORT----------------------------------------
        for i in range(0, len(library_num) - 1):#outter loop
            
            for index in range(0, len(library_num) - 1):#inner loop

               
               #below if statement determines the sort

              #list used is the list being sorted

               # > is for increasing order, < for decreasing

               if(library_num[index] > library_num[index + 1]):

                   

                    #if above is true, swap places!
                    swap(index,library_num)
 
                   #swap all other values
                    swap(index,titles)
                    swap(index,authors)
                    swap(index,genres)
                    swap(index,pages)
                    swap(index,status)

        
        #binary search
        search = input("Enter the library number you are looking for: ").lower()

        min = 0
        max = len(library_num) - 1
        mid = int((min + max) / 2)

        while min < max and search != library_num[mid]:
            if search < library_num[mid]:
                max = mid - 1
            else:
                min = mid + 1

            mid = int((min + max) / 2)

        if search == library_num[mid]:

            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
            
            print(f"{library_num[mid]:5} {titles[mid]:25} {authors[mid]:15} {genres[mid]:20} {pages[mid]:5} {status[mid]}") 

        else:
            print(f"Your search for {search} came up empty")

    elif search_type == "6":
        # SEQUENTIAL SEARCH: 


        found = [] 
        

        for i in range(0,len(status)):
           
            if "available" in status[i].lower():
                found.append(i)

        if not found:
            print(f"no books are available at this time")
        else:
            
           
            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
        for i in range(0, len(found)):
            print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5} {status[found[i]]}") 
    
    elif search_type == "7":
        # SEQUENTIAL SEARCH: 


        found = [] 
        

        for i in range(0,len(status)):
           
            if "on loan" in status[i].lower():
                found.append(i)

        if not found:
            print(f"no books are on loan at this time")
        else:
                
            print(f" {'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRE':18} {'PAGES':5} {'STATUS'}")
            print("---------------------------------------------------------------------------------")
        for i in range(0, len(found)):
            print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5} {status[found[i]]}") 

    elif search_type == "8":
        ans = "n"