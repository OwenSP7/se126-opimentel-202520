# final project

#Owen Pimentel
#3/03/25

# -------------------Program Prompt---------------------
#A DND 5e char creator that allows the user to pick a name, class ,race and stats. This info is then displayed back to the user along with their HP,AC, and Stat mods.

#-------------------Vars---------------------------------

#         
# stats     -       ste/dex/ini/wis/con/car - The characters attributes 
#charClass  -       The characters role
#race       -       The characters physical appearence and genetic 
#statMods   -       strMod/dexMod/intMod/wisMod/conMod/carMod - what you add to your roll involing stats
#raceName   -       The name of chosen Race
#className  -       the name of the chosen Class
#hp         -       health points
#ac         -       armor class
#name       -       the name enter by user
#startingGear   -   the equipment your class starts with


#---------------Imports---------------------------------
import csv

#----------------MAIN_CODE------------------------------

# Vars
ste = 0
dex = 0
ini = 0
wis = 0
con = 0
car = 0
ac = 10
hp = 0
level = 1
heavy = False
medium = False


print (f" Welcome to our Project!")

saveFile = input("Enter the relative path of the file you would like to load/save too: [make sure to filp forward slash to back slash]: ")


nameList = []
raceList = []
classList = []
levelList = []
strList = []
dexList = []
intList = []
wisList = []
conList = []
carList = []
strModList = []
dexModList = []
intModList = []
wisModList = []
conModList = []
carModList = []
hpList = []
acList = []
raceNameList = []
classNameList = []

with open(f"{saveFile}") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        nameList.append(rec[0])
        raceList.append(rec[1])
        classList.append(rec[2])
        levelList.append(rec[3])
        strList.append(rec[4])
        dexList.append(rec[5])
        intList.append(rec[6])
        wisList.append(rec[7])
        conList.append(rec[8])
        carList.append(rec[9])
        strModList.append(rec[10])
        dexModList.append(rec[11])
        intModList.append(rec[12])
        wisModList.append(rec[13])
        conModList.append(rec[14])
        carModList.append(rec[15])
        hpList.append(rec[16])
        acList.append(rec[17])
        raceNameList.append(rec[18])
        classNameList.append(rec[19])

    print(f"{nameList}")

loadChoice = input("Would you like to load a Adventurer or make a new one? [Load = 1/New = 2]: ").lower()

if loadChoice == "1":
    
    saveNumber = int(input("Enter the row number of the character you want to load: ")) - 1  
   

    name = nameList[saveNumber]
    race = raceList[saveNumber]
    charClass = classList[saveNumber]
    level = levelList[saveNumber]
    ste = strList[saveNumber]
    dex = dexList[saveNumber]
    ini = intList[saveNumber]
    wis = wisList[saveNumber]
    con = conList[saveNumber]
    car = carList[saveNumber]
    strMod = strModList[saveNumber]
    dexMod = dexModList[saveNumber]
    intMod = intModList[saveNumber]
    wisMod = wisModList[saveNumber]
    conMod = conModList[saveNumber]
    carMod = carModList[saveNumber]
    hp = hpList[saveNumber]
    ac = acList[saveNumber]
    raceName = raceNameList[saveNumber]
    className = classNameList[saveNumber]





elif loadChoice == "2":

    #prompts user to enter charcter name
    name = input(f"  \nEnter your Adventurers name: ")

    # prompts user to enter class
    print (f" \nClass options:")
    print (f"----------------------")
    print (f"   Barbarian:  1")
    print (f"   Fighter:    2")
    print (f"   Rouge:      3")
    print (f"   Monk:       4")
    print (f"   Paladin:    5")
    print (f"   Ranger:     6")
    print (f"   Warlock:    7")
    print (f"   Cleric:     8")
    print (f"   Bard:       9")
    print (f"   Sorcerer:   10")
    print (f"   Druid:      11")
    print (f"   Wizard:     12")
    print (f"----------------------")
    charClass = input(f"\nSelect your Class: ")

    # prevents user from moving on with invaild inputs
    while float(charClass) > 12 or float(charClass) < 1:
        print("***INVALID CLASS***")
        charClass = input(f"\nSelect your Class: ")



    print (f" \nClass options:")
    print (f"----------------------")
    print (f"   Random Rolls:       1")
    print (f"   Choose Manually:    2")
    print (f"   Standard Array:     3")
    statRollMethod = input("How would you like your stats?: ")

    while float(statRollMethod) > 3 or float(statRollMethod) < 1:
        print("***INVALID CHOICE***")
        statRollMethod = input("How would you like your stats?: ")    

    # Rolls Stats for the Char and displays them to user
    print (f"Lets see your Adventurers Attributes")
    import random

    #Have the stats randomly generated 
    if statRollMethod == "1":
        ste =(random.randrange(1,20))
        dex =(random.randrange(1,20))
        ini =(random.randrange(1,20))
        wis =(random.randrange(1,20))
        con =(random.randrange(1,20))
        car =(random.randrange(1,20))
        statSelection = ("Random")
        
    #Have the user manually select stats
    elif statRollMethod == "2":
        ste = float(input("What do you want for your Strength Stat (1-20): "))
        dex = float(input("What do you want for your Dexterity Stat (1-20): "))
        ini = float(input("What do you want for your Intelligents Stat (1-20): "))
        wis = float(input("What do you want for your Wisdom Stat (1-20): "))
        con = float(input("What do you want for your Constitution Stat (1-20): "))
        car = float(input("What do you want for your Charisma Stat (1-20): "))
        statSelection = "Manual"

    #Have the stats pre-selected vis optimal Standard Array
    elif statRollMethod == "3": 
        if charClass == "1":
            ste = 15
            dex = 14
            ini = 8
            wis = 12
            con = 14
            car = 10

        if charClass == "2":
            ste = 15
            dex = 8
            ini = 10 
            wis = 13
            con = 14
            car = 12

        elif charClass == "5":
            ste = 15
            dex = 8
            ini = 10 
            wis = 12
            con = 13
            car = 14

        elif charClass ==   "6":
            ste = 10
            dex = 15
            ini = 12
            wis = 13
            con = 14
            car = 8

        elif charClass == "3":
            ste = 8
            dex = 15
            ini = 10
            wis = 13
            con = 14
            car = 12


        elif charClass == "4":
            ste = 12
            dex = 15
            ini = 10 
            wis = 13
            con = 14
            car = 8

        
        elif charClass == "7":
            ste = 8
            dex = 13
            ini = 12
            wis = 10
            con = 14
            car = 15

        elif charClass == "8":
            ste = 12
            dex = 13
            ini = 10
            wis = 15
            con = 14
            car = 8


        elif charClass == "9":
            ste = 8
            dex = 14
            ini = 10 
            wis = 12
            con = 13
            car = 15


        elif charClass == "11":
            ste = 10
            dex = 13
            ini = 12
            wis = 15
            con = 14
            car = 8


        elif charClass == "10":
            ste = 8
            dex = 13
            ini = 12
            wis = 10
            con = 14
            car = 15


        elif charClass == "12":
            ste = 8
            dex = 13
            ini = 15
            wis = 12
            con = 14
            car = 10
        
        statSelection = "Standard"

            
    # displays the stat option that has been selected
    print (f"------------------------")
    print (f"\nHere are your {statSelection} Stats: ")
    print (f"\nStrength:      {ste:.0f}")
    print (f"Dexterity:     {dex:.0f}")
    print (f"Intelligence:  {ini:.0f}")
    print (f"Wisdom:        {wis:.0f}")
    print (f"Constitution:  {con:.0f}")
    print (f"Charisma:      {car:.0f}")
    print (f"------------------------")

    input(f" Press enter to continue")

    # prompts user to enter race
    print (f"\nRace Options: ")
    print (f"----------------------")
    print (f"Human:      1")
    print (f"DragonBorn: 2")
    print (f"Dwarf:      3")
    print (f"Elf:        4")
    print (f"Gnome:      5")
    print (f"Half Elf:   6")
    print (f"Halfling:   7")
    print (f"Half-Orc:   8")
    print (f"Tiefling:   9")
    print (f"----------------------")

    race = input(f"\nSelect your Race: ")

    # prompts user to re-enter race if they enter a invalid input 
    while float(race) > 9 or float(race) < 1:
        print("***INVALID RACE***")
        race = input(f"\nSelect your race: ")

    # add bonuses from races to stats
    if race == "1":
        ste += 1
        dex += 1
        ini += 1
        wis += 1
        con += 1
        car += 1
        raceName = "Human"

    elif race == "2":
        ste += 2 
        car += 1
        raceName = "Dragonborn"

    elif race == "3":
        con += 2
        raceName = "Dwarf"

    elif race == "4":
        dex += 2
        raceName = "Elf"

    elif race == "5":
        ini += 2
        raceName = "Gnome"

    elif race == "6":
        car += 2
        raceName = "Half-Elf"

    elif race == "7":
        dex+= 2
        raceName = "Halfling"

    elif race == "8":
        ste += 2 
        con += 1
        raceName = "Half-Orc"

    elif race == "9":
        car += 2
        ini += 1
        raceName = "Tiefling"
        
    # calculates the stat mods. Used for later calculations
    strMod = (ste - 10) / 2
    dexMod = (dex - 10) / 2
    intMod = (ini - 10) / 2
    wisMod = (wis - 10) / 2
    conMod = (con - 10) / 2
    carMod = (car - 10) / 2

    # calculations for HP and AC. also converts number from menu to name for display and starting equipment
    if charClass == "1":
        hp = 12 +  conMod
        ac += conMod
        className = "Barbarian"
        startingGear = ("Greataxe, 4 Handaxes and an Explorers Pack")

    elif charClass == "2" or charClass == "5"  or charClass == "6":
        hp = 10 + conMod

        if charClass == "2":
            className = "Fighter"
            startingGear = ("Chain Mail, Greatsword, Flail, 8 Javelins, Dungeoneer's Pack")
            heavy = True

        elif charClass == "5":
            className = "Paladin"
            startingGear = ("Chain Mail, Shield, Longsword, 6 Javelins, Holy Symbol, Priest's Pack")
            heavy = True

        elif charClass == "6":
            className = "Ranger"
            startingGear = ("Studded Leather Armor, Scimitar, Shortsword, Longbow, 20 Arrows, Quiver, Druidic Focus (sprig of mistletoe), Explorer's Pack")

    elif charClass == "3" or charClass == "4" or charClass == "7" or charClass == "8" or charClass == "9" or charClass == "11":
        hp = 8 + conMod
        
        if charClass == "3":
            className = "Rouge"
            startingGear = ("Leather Armor, 2 Daggers, Shortsword, Shortbow, 20 Arrows, Quiver, Thieves Tools, Burglar's Pack,")

        elif charClass == "4":
            className = "Monk"
            startingGear = ("Spear, 5 Daggers, Artisan's Tools or Musical Instrument chosen for the tool proficiency above, Explorer's Pack")
            ac += dexMod
        
        elif charClass == "7":
            className = "Warlock"
            startingGear = ("Leather Armor, Sickle, 2 Daggers, Arcane Focus (orb), Book (occult lore), Scholar's Pack")

        elif charClass == "8":
            className = "Cleric"
            startingGear = ("Chain Shirt, Shield, Mace, Holy Symbol, Priest's Pack")
            medium = True

        elif charClass == "9":
            className = "Bard"
            startingGear = ("Leather Armor, 2 Daggers, Musical Instrument of your choice, Entertainer's Pack")

        elif charClass == "11":
            className = "Druid"
            startingGear = ("Leather Armor, Shield, Sickle, Druidic Focus (Quarterstaff), Explorer's Pack, Herbalism Kit")
            
    elif charClass == "10" or charClass == "12":
        hp = 6 + conMod

        if charClass == "10":
            className = "Sorcerer"
            startingGear = ("Spear, 2 Daggers, Arcane Focus (crystal), Dungeoneer's Pack")
            

        elif charClass == "12":
            className = "Wizard"
            startingGear = ("2 Daggers, Arcane Focus (Quarterstaff), Robe, Spellbook, Scholar's Pack")
            

    # armor weight affects dex mod bonus for AC. This calculates dex mod bonus acording to armor weight
    if heavy == False: 
        ac += dexMod

    elif medium == True and (dex == 12 or dex == 13):
        ac += 1
        
    elif medium == True and dex >= 13:
        ac += 2




# basic character sheet
print(f"  \nHere's your Adventurer:")
print(f"-------------------------------")

print (f"\nName: {name}")
print (f"\nRace: {raceName}")
print (f"\nClass: {className}")
print (f"\nLevel: {level}")
print (f"\n------------------------------------------------")
print ("\nStats:")

print (f"\nStrength:          {ste:.0f}({strMod:.0f})")
print (f"Dexterity:         {dex:.0f}({dexMod:.0f})")
print (f"Intelligence:      {ini:.0f}({intMod:.0f})")
print (f"Wisdom:            {wis:.0f}({wisMod:.0f})")
print (f"Constitution:      {con:.0f}({conMod:.0f})")
print (f"Charsima:          {car:.0f}({carMod:.0f})")
print (f"\nHP:                {hp:.0f}")
print (f"AC:                {ac:.0f}")
print(f"\n-------------------------------------------------")

print(f"\nStarting Equipment: {startingGear}")

print(f"\n-------------------------------------------------")

answer = "n"

## trap loop for invalid input
answer = input ("Do you want to level up? [y/n]: ").lower()
while answer != "y" and answer != "n" :
        print("***INVALID CHOICE***")
        answer = input("Would you like to Level Up again? [y/n]: ").lower()

# leveling up which is increasing hp and what ever 2 stats you'd like to increase up till level 20
while answer == "y":
    level += 1
    print("Your level went up by 1!")
    
    # Hp gained per level is deterimed by class.
    if charClass == "1":
        hp += 7

        if level == 20:
            ste += 4
            dex += 4
        

    elif charClass == "3" or charClass == "4" or charClass == "7" or charClass == "8" or charClass == "9" or charClass == "11":
        hp += 5

    elif charClass == "2" or charClass == "5"  or charClass == "6":
        hp += 6 

    elif charClass == "10" or charClass == "12":
        hp += 4   

    ## Stat increases are given on these level milestones
    if level == 4 or level == 8 or level == 12 or level == 16 or level == 19:
        print (f"\nStat increase!: ")
        print (f"----------------------")
        print (f"Strength:      1")
        print (f"Dexterity:     2")
        print (f"Intelligence:  3")
        print (f"Wisdom:        4")
        print (f"Constitution:  5")
        print (f"Charsima:      6")
        print (f"----------------------")

  

        print("You can increase any stat by 2 or two stats by 1!")

        statUp = input("Choose the 1st stat you would like to improve?: ")

        if statUp == "1":
            ste += 1
        
        elif statUp == "2":
            dex += 1

        elif statUp == "3":
            ini += 1
        
        elif statUp == "4":
            wis += 1

        elif statUp == "5":
            con += 1

        elif statUp == "6":
            car += 1

        ## trap loop for invalid input
        while float(statUp) > 6 or float(statUp) < 1:
            print("***INVALID CHOICE***")
            statUp = input ("Choose the 1st stat you would like to improve?: ")

        statUp = input ("Choose the 2nd stat you would like to improve?: ")
        if statUp == "1":
            ste += 1

        elif statUp == "2":
            dex += 1

        elif statUp == "3":
            ini += 1

        elif statUp == "4":
            wis += 1

        elif statUp == "5":
            con += 1

        elif statUp == "6":
            car += 1


        ## trap loop for invalid input
        while float(statUp) > 6 or float(statUp) < 1:
            print("***INVALID CHOICE***")
            statUp = input ("Choose the 2nd stat you would like to improve?: ")

    answer = input("Would you like to Level Up again? [y/n]: ")
    
    ## trap loop for invalid input
    while answer != "y" and answer != "n" :
        print("***INVALID CHOICE***")
        answer = input("Would you like to Level Up again? [y/n]: ")

    ## level 20 is the max level
    if level == 20:
        answer = "n"    
        

# post level up character sheet
print(f"  \nHere's your Adventurer:")
print(f"-------------------------------")

print (f"\nName:  {name}")
print (f"\nRace:  {raceName}")
print (f"\nClass: {className}")
print (f"\nLevel: {level}")
print (f"\n------------------------------------------------")
print ("\nStats:")

print (f"\nStrength:          {ste:.0f}({strMod:.0f})")
print (f"Dexterity:         {dex:.0f}({dexMod:.0f})")
print (f"Intelligence:      {ini:.0f}({intMod:.0f})")
print (f"Wisdom:            {wis:.0f}({wisMod:.0f})")
print (f"Constitution:      {con:.0f}({conMod:.0f})")
print (f"Charsima:          {car:.0f}({carMod:.0f})")
print (f"\nHP:                 {hp:.0f}")
print (f"AC:                 {ac:.0f}")
print(f"\n-------------------------------------------------")

print(f"\nStarting Equipment: {startingGear}")

print(f"\n-------------------------------------------------")    
  
saveChoice = input("Would you like to save your Adventurer? [y/n]: ")

nameList.append(name)
raceList.append(race)
classList.append(charClass)
levelList.append(level)
strList.append(ste)
dexList.append(dex)
intList.append(ini)
wisList.append(wis)
conList.append(con)
carList.append(car)
strModList.append(strMod)
dexModList.append(dexMod)
intModList.append(intMod)
wisModList.append(wisMod)
conModList.append(conMod)
carModList.append(carMod)
hpList.append(hp)
acList.append(ac)
raceNameList.append(raceName)
classNameList.append(className)

if saveChoice in "y":

    

    file = open(f'{saveFile}', "w")

    for i in range(0,len(nameList)):
        file.write(f"{nameList[i]},{raceList[i]},{classList[i]},{levelList[i]},{strList[i]},{dexList[i]},{intList[i]},{wisList[i]},{conList[i]},{carList[i]},{strModList[i]},{dexModList[i]},{intModList[i]},{wisModList[i]},{conModList[i]},{carModList[i]},{hpList[i]},{acList[i]},{raceNameList[i]},{classNameList[i]}\n")   
else:
    print()

