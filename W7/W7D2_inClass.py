#W7D2 - live class: demo

def menu():
    print("simple menu")
    print("1. SEARCH BY NAME")
    print("2. SEARCH BY NUM")
    print("3. SEARCH BY COLOR")
    print("4. EXIT")

    return input("Enter your search type [1-4]: ")

def swap(index, listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp

import csv

#create the lists
names = []
nums = []
colors = []

valid_menu = ["1","2","3","4"]

with open("W2/simple.csv") as csvfile:
    files = csv.reader(csvfile)

    for rec in files:
        names.append(rec[0])
        nums.append(rec[1])
        colors.append(rec[2])
    #disconnected from file----------------

ans = "y"

while ans == "y":
    choice = menu()

    if choice not in valid_menu:
        print("!Invalid entry!")

    elif choice == "1":
        print("\n -search by name-")


        for i in range(len(names) - 1):
            for j in range(len(names) -1):
                #to see if larger value comes before smaller value
                if names[j] > names[j + 1]:
                    #swap places! - not just this value, but all ASSOCIATED values!
                    swap(j, names)
                    swap(j, colors)
                    swap(j, nums)

        min = 0
        max = len(names) -1
        mid = int((min + max) /2)

        search = input("Enter the name your looking for: ")

        while min < max and search.lower() != names[mid].lower():
            if search.lower() < names[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) /2)        

        if search.lower() == names[mid].lower():
            print(f"{search} was found")
           
            print(f"{names[mid]:8}   {nums[mid]:3}    {colors[mid]:}")
        else:
             print(f"{search} was not found")

    

    elif choice == "2":
        print("\n -search by num-")

    elif choice == "3":
        print("\n -search by color-")   


        for i in range(len(colors) - 1):
            for j in range(len(colors) -1):
                #to see if larger value comes before smaller value
                if colors[j] > colors[j + 1]:
                    #swap places! - not just this value, but all ASSOCIATED values!
                    swap(j, colors)
                    swap(j, names)
                    swap(j, nums)

        print("\n -search by name-")

        min = 0
        max = len(colors) -1
        mid = int((min + max) /2)

        search = input("Enter the color your looking for: ")

        while min < max and search.lower() != colors[mid].lower():
            if search.lower() < colors[mid].lower():
                max = mid - 1
            else:
                min = mid + 1
            mid = int((min + max) /2)        

        if search.lower() == colors[mid].lower():
            print(f"{search} was found")
           
            print(f"{names[mid]:8}   {nums[mid]:3}    {colors[mid]:}")
        else:
             print(f"{search} was not found")            



    elif choice == "4":
        print("\n -exit-")    
        ans = "x" 



#-----2d lists---------------

dataFile = [
    #this will be 2d lists
    names, # list of names
    nums,
    colors 
]


print("\n\nData file (2dlist[][]):")
for i in range(0, len(dataFile)):
    #asscessing each list within the 2D list datafiles
    print(f"INDEX {i} of 'datafile': {dataFile[i]}")
    for j in range(0, len(dataFile[i])):
        #asscessing each value within the list currently looked at from outer for loop
        print(f"INDEX {i} and value DataFile[{j}]: {dataFile[i][j]}")