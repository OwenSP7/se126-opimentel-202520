# W4D2 - Demo
# 1/28/25
# Owen Pimentel

#----------Program prompt----------

#review for using sequenstial search and create and write data to txt file

#---IMPORTS----------------------------------
import csv


#-------Functions----------


    

#-------Main Code--------------

dragons =[]
riders = []
count = []
color1 =[]
color2 = []


with open("W4/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        
        elif rec[2] == "1":
            color2.append("---")
        else:
            color2.append("error")
# disconnected from file. can be used later

# process loop for display

print(f"{"DRAGONS":15} {"RIDER":30} {"#":3} {"COLOR1":8} {"COLOR2"}")
print("-------------------------------------------------------------------------------------")

for i in range(0, len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")


#Search for a drago

found = "x"
search = input("Which dragon are you looking for: ")

#search for a color set
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        found = i

# display resault
if found != "x":
    print(f"your search for {search} was FOUND")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]:8}")
else:
   print(f"your search for {search} was NOT FOUND")

#write some data to new file

#search for color set
found = []
search = input("enter the dragon color you are looking for: ")

for i in range(0,len(color1)):
    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)
    
if not found:
    print(f"your search for {search} was NOT FOUND")
else:
    for i in range(0, len(found)):
        print(f"your search for {search} was FOUND")
        print(f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]:8}")

#write date to file
file = open('W4/test.csv', "w")

for i in range(0,len(dragons)):
    file.write((f"{dragons[i]},{riders[i]}\n"))


file.write("Hello World")
file.close()