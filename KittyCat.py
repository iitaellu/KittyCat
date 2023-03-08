#This base structure is from course material

import sqlite3
db = sqlite3.connect('KittyCatInfo.db') #Own file name
cur = db.cursor()
def initializeDB():
    try:
        f = open("data.sql", "r")
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
        print("6: Search for one cat, its winned show(s)")
        print("7: Modify user information")
        print("0: Quit")
        userInput = input("What do you want to do? ")
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
            catShowWinner()
        if userInput == "7":
            updateUserInfo()
        if userInput == "0":
            print("Ending software...")
    db.close()        
    return

def searchBreed():
    breedName = input("Give the breed name ID (for example: MAU): ")

    try:
        cur.execute(
            "SELECT * FROM BreedInfo WHERE FK_breedID = (?);", (breedName,))
        oneRow = cur.fetchone()

        print("Descript:"+str(oneRow[1]))
        print("Coat lenght:"+str(oneRow[2]))
        print("Coat pattern:"+str(oneRow[3]))
        print("Location of origin:"+str(oneRow[4]))
        print("Registered number: "+str(oneRow[5]))
    except:
        print("Not found try again")

    return


def printTopRanking():
    showName = input("What is the cat show name? ")

    try:
        cur.execute("SELECT score, catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top1=catID WHERE showName=(?);", (showName,))
        oneRow = cur.fetchone()
        print(showName, " Score:"+str(oneRow[0]))
        print("The 1.st:"+str(oneRow[1]))
        cur.execute(
            "SELECT catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top2=catID WHERE showName=(?);", (showName,))
        twoRow = cur.fetchone()
        print("The 2.st:"+str(twoRow[0]))
        cur.execute(
            "SELECT catName FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top3=catID WHERE showName=(?);", (showName,))
        threeRow = cur.fetchone()
        print("The 3.st:"+str(threeRow[0]))
    except:
        print("Not found try again")

    return


def printOwnCats():
    owner = input("What is your last name? ")

    try:
        print("Printing your cat(s)")
        for row in cur.execute("SELECT catName FROM Cat INNER JOIN Owners ON ownerID=FK_ownerID WHERE ownerName LIKE (?);", ("%"+owner+"%",)):
            print(row)
    except:
        print("Not found try again")

    return


def printOneCat():
    ownerName = input("Give your name: ")
    catName = input("What is the cat's name? ")

    try:
        cur.execute("SELECT Cat.catName, Breed.breedName, Cat.age from Cat INNER JOIN 'Breed' ON Cat.FK_breedID = Breed.breedID \
                    INNER JOIN 'Owners' ON Cat.FK_ownerID = Owners.ownerID WHERE Cat.catName LIKE (?) AND Owners.ownerName LIKE (?);", ("%"+catName+"%", "%"+ownerName+"%",))

        # WHERE catName = "Bob" AND ownerName = "S. Jokunen"
        oneRow = cur.fetchone()

        print(catName+"'s information")
        print("Name: "+str(oneRow[0]))
        print("Breed: "+str(oneRow[1]))
        print("Age: "+str(oneRow[2]))

    except:
        print("Not found try again")

    return

def updateCatInfo():
    userInput = -1

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
    catName= input("     What is the cat's name? ")
    cur.execute("SELECT count(*) FROM Cat")
    catId = list(cur)[0][0]+1
    catBreed= input("     What is the cat breed? ")
    
    catAge = input("     How old is the cat? ")

    owner = input("     What is your last name? (in form F. Lastname) ")
    cur.execute("SELECT ownerID FROM 'Owners' WHERE ownerName LIKE (?)", ("%"+owner+"%",))
    oneRow=cur.fetchone()
    if (oneRow == None):
        cur.execute("Select count(*) From Owners")
        number_of_owners=list(cur)[0][0]
        ownerId=number_of_owners + 1
        cur.execute("INSERT INTO 'Owners' VALUES((?),(?),(?),(?),(?))", (ownerId, owner, "-", "-", "-",))
        db.commit()
        print("     New owner added. Please modify your information and add phone number, email and country")
    if (oneRow != None):
        ownerId=(oneRow[0])


    cur.execute("SELECT breedID FROM 'Breed' WHERE breedName = (?)", (catBreed,))
    otherRow=cur.fetchone()
    breedId = otherRow[0]

    cur.execute("INSERT INTO 'Cat' VALUES ((?),(?),(?),(?),(?))", (catId, ownerId, breedId, catName, catAge,))
    db.commit()
    print("     Cat named "+ catName + " added")

    return

def updateCat():
    owner = input("     What is your last name? ")
    catName= input("     What is the cat's name you want to modify? ")

    cur.execute("SELECT Cat.catID, Owners.ownerID FROM CAT INNER JOIN 'Owners' ON Cat.FK_ownerID = Owners.ownerID WHERE ownerName LIKE (?) AND catName = (?)", ("%"+owner+"%", catName,))
    oneRow=cur.fetchone()

    catId= oneRow[0]
    ownerId = oneRow[1]

    catNewName= input("     What is the cat's new name (N=no change) ")
    newOwner= input("     What is cat's new owner's name? (in form F. Lastname) (N=no change) ")
    catAge = input("     How old is the cat? (N=no change) ")
    catBreed= input("     What is the new breed of cat? (N=no change) ")

    if ((catNewName != 'N') and (catNewName != 'n')):
            cur.execute("UPDATE 'CAT' set catName = (?) WHERE FK_ownerid = (?) AND catID = (?)", (catNewName, ownerId, catId,))
            db.commit()
            print("     Cat name changed")
    
    if ((newOwner != 'N') and (newOwner != 'n')):
        cur.execute("SELECT ownerID FROM OWNERS WHERE ownerName = (?)", (newOwner,))
        ownerInfoRow = cur.fetchone()
        if (ownerInfoRow != None):
            newOwnerId = ownerInfoRow[0]
            cur.execute("UPDATE 'CAT' set FK_ownerID = (?) WHERE FK_ownerID = (?) AND catID = (?)", (newOwnerId, ownerId, catId,))
            db.commit()
            print("     New owner set")
        else: 
            print("     Can't find new owner from db, return to menu...")
    if ((catAge != 'N') and (catAge != 'n')):
        cur.execute("UPDATE 'CAT' set Age = (?) WHERE FK_ownerid = (?) AND catID = (?)", (int(catAge), ownerId, catId,))
        db.commit()
        print("     Cat's age changed")
    
    if ((catBreed != 'N') and (catBreed != 'n')):
            cur.execute("SELECT breedID FROM Breed WHERE breedName = (?)", (catBreed,))
            breedRow = cur.fetchone()
            breedID = breedRow[0]
            cur.execute("UPDATE 'CAT' set FK_breedID = (?) WHERE FK_ownerid = (?) AND catID = (?)", (breedID, ownerId, catId,))
            db.commit()
            print("     Cat's breed changed")
    return

def deleteCat():
    catName= input("     What is the cat's name? ")
    ownerName = input ("     What is your last name? ")

    cur.execute("SELECT Cat.catID, Owners.ownerID FROM CAT INNER JOIN 'Owners' ON Cat.FK_ownerID = Owners.ownerID WHERE ownerName LIKE (?) AND catName = (?)", ("%"+ownerName+"%", catName,))
    oneRow=cur.fetchone()

    catID = oneRow[0]
    ownerId = oneRow[1]

    cur.execute("DELETE FROM 'Cat' WHERE catID = (?) AND FK_ownerID = (?)", (catID, ownerId,))
    db.commit()

    print("     Cat deleted")
    return


def catShowWinner():
    print("All participant from different shows:")

    for row in cur.execute("SELECT catName FROM Cat"):
        print(row)

    catName = input("Give the cat name: ")
    win = 0
    print("Winned shows: ")
    for row in cur.execute("SELECT showName FROM Shows INNER JOIN Ranking ON FK_showID = showID INNER JOIN Cat ON catID = top1  WHERE  catName = (?);", (catName,)):
        if len(row) >= 1:
            print(row)
            win = 1

    if win == 0:
        print("None")

    return

def updateUserInfo():
    userInput = -1

    while(userInput != "0"):
        print("     \nMenu options:")
        print("     1: Add new user")
        print("     2: Update user info")
        print("     3: Delete user")
        print("     0: Quit")
        userInput = input("     What do you want to do? ")
        if userInput == "1":
            addUser()
        if userInput == "2":
            updateUser()
        if userInput == "3":
            deleteUser()
        if userInput == "0":
            print("     Returning...")
    #Modify userinfo?
    return

def addUser():
    return

def updateUser():
    return

def deleteUser():
    return


main()
