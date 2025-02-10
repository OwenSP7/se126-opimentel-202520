# W6D1 - Demo
# 2/10/25
# Owen Pimentel



#-------IMPORTS----------------------------------
import csv


#---------------------------------------------

library_num = []
titles = []
authors = []
genres = []
pages = []

# open file
with open("W6/library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    #create lists
    for rec in file:
        library_num.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

print(f"{"LIB#":5} {"TITLE":25} {"AUTHOR":15} {"GENRE":20} {"PAGES":5}")
print("------------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(library_num)):
    print(f"{library_num[i]:5} {titles[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5}")       


# SEQUENTIAL SEARCH: allow user to search for a title


seq_count = 0
found = [] 
search_num = input("Which Library Num are you looking for: ")

for i in range(0,len(library_num)):
    seq_count += 1
    if search_num in library_num[i]:
        found.append(i)

if not found:
    print(f" Search not found for {search_num} was not found")
else:
    print(f"Search found for {search_num}")
    print (f"SEQ COUNT:{seq_count} ")
    print(f"{"LIB#":5} {"TITLE":25} {"AUTHOR":15} {"GENRE":20} {"PAGES":5}")
print("------------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(found)):
    print(f"{library_num[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]:15} {genres[found[i]]:20} {pages[found[i]]:5}") 


# BI SEARCH

min = 0
max = len(library_num) - 1
mid = int((min+ max) / 2)

bin_count = 0

while min < max and search_num != library_num[mid]:
    #list has not been exhausted of potential values yet

    if search_num < library_num[mid]:
        # everythiung after mid point is not possible
        max = mid - 1

    else:
        # everythiung before mid point is not possible
        min = max + 1

    mid = int((min + max) / 2)
    bin_count += 1



print(f" BIN COUNT: {bin_count}")

if search_num == library_num[mid]:

    print(f"Search found for {search_num}")

    print(f"{"LIB#":5} {"TITLE":25} {"AUTHOR":15} {"GENRE":20} {"PAGES":5}")

    print(f"{library_num[mid]:5} {titles[mid]:25} {authors[mid]:15} {genres[mid]:20} {pages[mid]:5}") 

else:
    print(f" Search not found for {search_num} was not found")

