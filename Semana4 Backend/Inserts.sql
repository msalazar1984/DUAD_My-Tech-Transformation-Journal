-- SQLite
INSERT INTO Books (Name, Author)
    VALUES ('Don Quijote',1);

INSERT INTO Books (Name, Author)
    VALUES ('La Divina Comedia',2);

INSERT INTO Books (Name, Author)
    VALUES ('Vagabond 1-3',3);

INSERT INTO Books (Name, Author)
    VALUES ('Dragon Ball',4);

INSERT INTO Books (Name, Author)
    VALUES ('The Book of the 5 Ring',NULL);

INSERT INTO Authors (Name)
    VALUES ('Miguel de Cervantes');

INSERT INTO Authors (Name)
    VALUES ('Dante Alighieri');

INSERT INTO Authors (Name)
    VALUES ('Takehiko Inoue');

INSERT INTO Authors (Name)
    VALUES ('Akira Toriyama');

INSERT INTO Authors (Name)
    VALUES ('Walt Disney');

INSERT INTO Customers (Name,Email)
    VALUES ('John Doe','j.doe@email.com');

INSERT INTO Customers (Name,Email)
    VALUES ('Jane Doe','jane@doe.com');

INSERT INTO Customers (Name,Email)
    VALUES ('Luke Skywalker','darth.son@email.com');

INSERT INTO Rents (BookID,CustomerID,State)
    VALUES (1,2,'Returned');

INSERT INTO Rents (BookID,CustomerID,State)
    VALUES (2,2,'Returned');

INSERT INTO Rents (BookID,CustomerID,State)
    VALUES (1,1,'On Time');

INSERT INTO Rents (BookID,CustomerID,State)
    VALUES (3,1,'On Time');

INSERT INTO Rents (BookID,CustomerID,State)
    VALUES (2,2,'Overdue');
