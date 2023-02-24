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
    FK_ownerId int NOT NULL,
    FK_breedID Varchar(3),
    catName Varchar(30),
    age int,
    Primary Key (catID),
    Foreign Key (FK_ownerID) REFERENCES Owner (ownerID),
    Foreign Key (FK_breedID) REFERENCES Breed (breedID)
};

CREATE TABLE BreedInfo {
    FK_breedID varchar(3) NOT NULL,
    descript varchar(500),
    coat_len varchar(30),
    coat_pattern varchar(30),
    catType varchar(30),
    numOfCats int,
    Foreign Key (FK_breedID) REFERENCES Breed(breedID)
};

CREATE TABLE Shows {
    showID int NOT NULL,
    showName varchar(30),
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

INSERT INTO Owners VALUES (1,"M. Smith","0400 000 3343","m.smith@email.com","Canada");
INSERT INTO Owners VALUES (2,"S. Jokunen","0400 323 5553","s.jokunen@email.com","Finland");
INSERT INTO Owners VALUES (3,"T. Tarantino","0500 030 0032","t.tarantino@email.com","Italia");
INSERT INTO Owners VALUES (4,"L. Yang","3003 400 3000","l.yang@email.com","Cina");
INSERT INTO Owners VALUES (5,"G. Fyodorov","9999 039 2233","g.fyodorov@email.com","Russia");
INSERT INTO Owners VALUES (6,"G. Leitzke","0030 032 4432","g.leitzke@email.com","Germany");
INSERT INTO Owners VALUES (7,"J. Kunkle","0030 287 8878","j.kunkle@emial.com","Germany");
INSERT INTO Owners VALUES (8,"N. Chou","3003 998 9992","n.chou@email.com","China");
INSERT INTO Owners VALUES (9,"W.-J. Chung","9983 993 2334","w-j.chung@email.com","Korea");
INSERT INTO Owners VALUES (10,"E. Salo","0400 994 030","e.salo@email.com","Finland");


INSERT INTO Breed VALUES ("ABY","Abyssinian");
INSERT INTO Breed VALUES ("BEN","Bengal");
INSERT INTO Breed VALUES ("MAU","Egyprian Mau");
INSERT INTO Breed VALUES ("MCO","Maine Coon");
INSERT INTO Breed VALUES ("NFO","Norwegian Forest Cat");
INSERT INTO Breed VALUES ("PER","Persian");
INSERT INTO Breed VALUES ("RAG","Ragdoll");
INSERT INTO Breed VALUES ("SPH","Sphynx");
INSERT INTO Breed VALUES ("SIA","Siamese");
INSERT INTO Breed VALUES ("SIB","Siberian");
INSERT INTO Breed VALUES ("THA","Thai");


INSERT INTO Cat VALUES (1,10,"RAG","Mittens",6);
INSERT INTO Cat VALUES (2,1,"BEN","Hockey",3);
INSERT INTO Cat VALUES (3,7,"MCO","Forest Junior",1);
INSERT INTO Cat VALUES (4,9,"SIA","Long",5);
INSERT INTO Cat VALUES (5,5,"SIB","Muddy",0);
INSERT INTO Cat VALUES (6,10,"RAG","Teddy",3);
INSERT INTO Cat VALUES (7,2,"NFO","Cute",7);
INSERT INTO Cat VALUES (8,4,"SPH","Muddy",5);
INSERT INTO Cat VALUES (9,9,"BEN","Bob",2);
INSERT INTO Cat VALUES (10,10,"MCO","Rex",10);




INSERT INTO BreedInfo VALUES ("","","","","",0);




INSERT INTO Shows VALUES (0,"",0,"");




INSERT INTO Ranking VALUES (0,0,0,0,0,"");
