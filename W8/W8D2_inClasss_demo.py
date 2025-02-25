# W6D1 - Demo
# 2/10/25
# Owen Pimentel



#-------IMPORTS----------------------------------
import csv


#---------------------------------------------

library = {
    #indexs are strings set by developer
    # "key value"
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}


# open file
with open("W8/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    #create lists
    for rec in file:
        #add each records data as a new key + value pair from the text file
        #key --> rec[0] ; value --> rec[1]
        library.update({rec[0] : rec[1]})
        # when using update() --> pass {'key : value}

# disconnect from file
print(f"{'KEY':6}\t{'TITLE'}")
print('-' * 50)
for key in library:
    #for every kay and value pair in the library dictionary
    print(f"{key:6}\t{library[key]}")
print('-' * 50)

#sequesntial search for a title
search = input("Enter the Title you are looking for: ")
found = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found titles location in the dic
        found = key
if found != 0:
    print(f"KEY: {key:6}\tTITLE: {library[found]}")
else:
    print("your search was not found")

#BINARY SEARCH for LIBRARY NUMBER
# in order to binary search a set of keys you must FIRST ...



        
