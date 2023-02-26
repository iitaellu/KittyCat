#This base structure is from course material

import sqlite3
db = sqlite3.connect('KittyCatInfo.db') #Own file name
cur = db.cursor()
def initializeDB():
    try:
        f = open("sqlcommands.sql", "r")
        commandstring = ""
        for line in f.readlines():
            commandstring+=line
        cur.executescript(commandstring)
    except sqlite3.OperationalError:
        print("Database exists, skip initialization")
    except:
        print("No SQL file to be used for initialization") 


def main():
    initializeDB()
    userInput = -1
    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Search for one breed info")
        print("2: Print top 3 ranking in a show")
        print("3: Print all your cat info")
        print("4: Print your cat info")
        print("5: Modify your cats info")
        print("6: Search for one breed, it's shows and ranking")
        print("7: Something")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            searchBreed()
        if userInput == "2":
            printTopRanking()
        if userInput == "3":
            printOwnCats()
        if userInput == "4":
            printOneCat()
        if userInput == "5":
            updateCatInfo()
        if userInput == "6":
            breedShowRanking()
        if userInput == "7":
            Something()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return


def searchBreed():
    breedName = input("Give the breed name ID (for example: MAU) : ")
    cur.execute("SELECT * FROM BreedInfo WHERE FK_breedID = (?);", (breedName,))
    oneRow=cur.fetchone()

    print("Descript:"+str(oneRow[1]))
    print("Coat lenght:"+str(oneRow[2]))
    print("Coat pattern:"+str(oneRow[3]))
    print("Location of origin:"+str(oneRow[4]))
    print("Registered number: "+(oneRow[5]))

    return

def printTopRanking():
    showName = input("What is the cat show name? ")

    cur.execute("SELECT score, catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top1=catID WHERE showName=(?);", (showName,))
    oneRow= cur.fetchone()
    print(showName," Score:"+str(oneRow[0]))
    print("The 1.st:"+str(oneRow[1]))
    cur.execute("SELECT catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top2=catID WHERE showName=(?);", (showName,))
    twoRow=cur.fetchone()
    print("The 2.st:"+str(twoRow[0]))
    cur.execute("SELECT catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top3=catID WHERE showName=(?);", (showName,))
    threeRow=cur.fetchone()
    print("The 3.st:"+str(threeRow[0]))

    return

def printOwnCats():
    owner= input("What is your last name? ")
    print("Printing your cat(s)")

    for row in cur.execute("SELECT * FROM Cat INNER JOIN Owners ON ownerID=FK_ownerID WHERE ownerName LIKE %(?)%;", (owner,)):
        print(row)
    
    return


def printOneCat():
    ownerName = input("Give your name (in form F. Lastname) ")
    catName = input("What is the cat's name? ")
    
    cur.execute("Cat.catName, Breed.breedName, Cat.age from Cat INNER JOIN 'Breed' ON Cat.FK_breedID = Breed.breedID INNER JOIN 'Owners' ON Cat.FK_ownerID = Owners.ownerID WHERE catName = (?) AND ownerName = (?)", (catName, ownerName,))

    #SELECT Cat.catName, Breed.breedName, Cat.age from Cat
    #INNER JOIN "Breed" ON Cat.FK_breedID = Breed.breedID
    #INNER JOIN "Owners" ON Cat.FK_ownerID = Owners.ownerID
    #WHERE catName = "Bob" AND ownerName = "S. Jokunen"
    oneRow=cur.fetchone()

    print(catName+"information")
    print("Name:"+(oneRow[0]))
    print("Owner:"+(oneRow[1]))
    print("Breed:"+(oneRow[2]))
    print("Age: "+(oneRow[4]))

    return

def updateCatInfo():

    while(userInput != "0"):
        print("\nMenu options:")
        print("1: Add new a cat")
        print("2: Update a cat info")
        print("3: Delete a cat")
        print("0: Quit")
        userInput = input("What do you want to do? ")
        print(userInput)
        if userInput == "1":
            addCat()
        if userInput == "2":
            updateCat()
        if userInput == "3":
            deleteCat()
        if userInput == "0":
            print("Returning...")

    return

def addCat():
    def addCat():
    catName= input("What is the cat's name? ")
    number_of_cats = cur.execute("SELECT * FROM Cat")
    catId = number_of_cats
    catBreed= input("What is the cat breed?")
    
    catAge = input("How old is the cat?")

    owner = input("What is your name? (in form F. Lastname) ")
    cur.execute("SELECT ownerID FROM 'Owners WHERE ownerName = (?)", (owner,))
    oneRow=cur.fetchone()
    if(oneRow[0] == Null):
        number_of_owners = cur.execute("Select * From Owners")
        ownerId=number_of_owners
        #NEW owner to Owner Table?
    else:
        ownerId=(oneRow[0])

    cur.execute("SELECT breedID FROM 'Breed' WHERE breedName = (?)", (catBreed))
    otherRow=cur.fetchone()
    breedId = otherRow[0]

    cur.execute("INSERT INTO 'Cat' VALUES ((?),(?),(?),(?),(?)", (catId, ownerId, breedId, catName, catAge,))
    print("Cat named (?) added", (catName,))

    return


    return

def updateCat():
    catName= input("What is the cat's name? ")
    catBreed= input("What is the new cat breed? (N=no change)")
    ownerId= input("What is the cat's new owner id? (N=no change)")
    catAge = input("How old is the cat? (N=no change)")


    return

def deleteCat():
    catName= input("What is the cat's name? ")

    
    return


def breedShowRanking():
    breedName = input("Give the breed name: ")
    showName = input ("Give the cat show name (N=gives all show breed has been)?")
    
    if(showName == "N"):
        cur.execute()
    else:
        cur.execute()

    #db.commit()

    return

def Something():
    
    return


main()
