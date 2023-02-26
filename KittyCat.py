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
            printOwnCat()
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

    cur.execute("SELECT * FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top1=catID WHERE showName=(?);", (showName,))
    oneRow= cur.fetchone()
    print(showName," Score:"+str(oneRow[10]))
    print("The 1.st:"+str(oneRow[14]))
    cur.execute("SELECT * FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top2=catID WHERE showName=(?);", (showName,))
    twoRow=cur.fetchone()
    print("The 2.st:"+str(twoRow[14]))
    cur.execute("SELECT * FROM Shows INNER JOIN Ranking ON FK_showID=showID INNER JOIN Cat ON top3=catID WHERE showName=(?);", (showName,))
    threeRow=cur.fetchone()
    print("The 3.st:"+str(threeRow[14]))

    return

def printOwnCat():
    print("Printing your cat(s)")

    for row in cur.execute('SELECT * FROM Cat'):
        print(row)
    
    return


def printOneCat():
    catName = input("What is the cat's name? ")
    
    cur.execute("SELECT * FROM Cat WHERE catName = ('"+catName+"');")
    oneRow=cur.fetchone()

    print(catName+"information")
    print("ID:"+(oneRow[0]))
    print("Owner ID:"+(oneRow[1]))
    print("Breed ID:"+str(oneRow[2]))
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
    catName= input("What is the cat's name? ")
    catId =#luo jollain random generaattorilla
    catBreed= input("What is the cat breed?")
    ownerId=# saadaan jostain
    catAge = input("How old is the cat?")


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
