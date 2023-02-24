CREATE TABLE Owners {
    ownerID int NOT NULL,
    ownerName Varchar(80),
    phone Varchar(30),
    email Varchar(80),
    Country Varchar(80),
    Primary Key (ownerID)
};

CREATE TABLE Breed {
    breedID Varchar(3) NOT NULL,
    breedName Varchar(30),
    Primary Key (breedID)
};

CREATE TABLE Cat {
    catID int NOT NULL,
    FK_ownerId int,
    FK_breedID Varchar(3),
    catName Varchar(30),
    age int,
    Primary Key (catID),
    Foreign Key (FK_ownerID) REFERENCES Owner (ownerID),
    Foreign Key (FK_breedID) REFERENCES Breed (breedID)
};

CREATE TABLE BreedInfo {
    FK_breedID varchar(3),
    descript varchar(500),
    coat_len varchar(30),
    coat_pattern varchar(30),
    catType varchar(30),
    numOfCats int,
    Foreign Key (FK_breedID) REFERENCES Breed(breedID)
};

CREATE TABLE Shows {
    showID int NOT NULL,
    place varchar(30),
    participants int,
    judges varchar(80),
    Primary Key (showID)
};

CREATE TABLE Ranking {
    rankingID int NOT NULL,
    FK_showID int,
    top1 int,
    top2 int,
    top3 int,
    score varchar(30),
    Primary Key (rankingID),
    Foreign Key (FK_showID) REFERENCES Shows(showID)
};

INSERT INTO Owners VALUES (0,"","","","");




INSERT INTO Breed VALUES ("","");




INSERT INTO Cat VALUES (0,0,"","",0);





INSERT INTO BreedInfo VALUES ("","","","","",0);




INSERT INTO Shows VALUES (0,"",0,"");




INSERT INTO Ranking VALUES (0,0,0,0,0,"");
