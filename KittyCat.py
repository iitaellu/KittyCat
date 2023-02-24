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
        print("5: Update your cat show info")
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
    breedName = input("Give the breed name: ")
    
    return

def printTopRanking():
    showName = input("What is the cat show? ")

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
