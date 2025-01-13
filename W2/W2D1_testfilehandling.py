#w2D1 - Text file handling - introduction

#import the csv
import csv


print(f"\n{'Name' :10} \t {'Num' :3} \t {'Color'}")
print("--------------------------------------------------")
total_records = 0 # the total number of records (rows) in the file

#connecting to file path - switch \ to /
with open("W2/simple.csv") as csvfile:
    #indent 1 level (new block)

    #allow processer to read file date
    file = csv.reader(csvfile)

    #loop through every record(row) in the file
    for record in file:

        #add +1 to total_records
        total_records +=1

        #print(record) # the list view of each record(row)

        name = record[0]
        number = record[1]
        color = record[2]

        print(f"{name:10} \t {number:3} \t {color}")

#-----------------disconnect from file------------------
print("--------------------------------------------------")

print(f"\nTOTAL RECORDS: {total_records}\n")