# W8D1 - Dictonaries : Intro Demo
# 2/24/25
# Owen Pimentel


#---------IMPORTS----------------------------------


#-------MAIN CODE----------------------------------------------------

#start by making a populated list
myCar = {
    #'key' : value,
    "make" : "Ford",
    "model" : "SE Hatchback",
    "year" : 2014,
    "name" : "Gwendoline",
    "color" : "black",
    #keys cannot be repeated/ no dupes allowed
    # repeats replace oringal value of key
}

#display the entire dictionary -> "myCar"
print(myCar)
#display just "make" and "model"
print(f" my car is a {myCar["make"]} {myCar["model"]}")

#dictinonaryName["keyword"] --> access stored value

#keys can not be reapeated within a dic, but they can be reused arcoss unique dic names: myCar vs yourCar
yourCar = {
    #'key' : value,
    "make" : "GMC",
    "model" : "Canyon",
    "year" : 2019,
    "name" : "Jolly",
    "color" : "black",
    "friends" : ["Ray", "Matt", "Duncan"]
    #keys cannot be repeated/ no dupes allowed
    # repeats replace oringal value of key
}

print(f"Robs car is a {yourCar["make"]} {yourCar['model']}")

#friends is a list, 2nd [] are used to point to which value in said list
print(f"{yourCar['friends'][2]}")

#processing through a dic and its keys
for key in yourCar:
    print(f"{key.upper()} : {yourCar[key]}")

#ass a key and value to a pre-existing dictionary
yourCar["plate"] = "12345"