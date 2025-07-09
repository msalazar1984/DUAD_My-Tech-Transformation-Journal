-- SQLite
SELECT Books.ID, Books.Name, Authors.Name 
    FROM Books
    INNER JOIN Authors
    ON Books.Author=Authors.ID;

SELECT Books.ID, Books.Name, Authors.Name 
    FROM Books
    LEFT JOIN Authors
    ON Books.Author=Authors.ID
    WHERE Books.Author IS NULL;

SELECT Authors.ID, Authors.Name, Books.Name 
    FROM Authors
    LEFT JOIN Books
    ON Books.Author=Authors.ID
    WHERE Books.Name IS NULL;

SELECT DISTINCT Rents.BookID,Books.Name
    FROM Rents
    INNER JOIN Books
    ON Rents.BookID=Books.ID;

SELECT DISTINCT Rents.BookID,Books.Name
    FROM Books
    LEFT JOIN Rents
    ON Rents.BookID=Books.ID
    WHERE BookID IS NULL;

SELECT DISTINCT Rents.CustomerID,Customers.Name
    FROM Rents
    INNER JOIN Customers
    ON Rents.CustomerID=Customers.ID;

SELECT DISTINCT Rents.CustomerID,Customers.Name
    FROM Customers
    LEFT JOIN Rents
    ON Rents.CustomerID=Customers.ID
    WHERE CustomerID IS NULL;

SELECT Rents.ID,Rents.BookID,Books.Name
    FROM Rents
    INNER JOIN Books
    ON Rents.BookID=Books.ID
    WHERE Rents.State='Overdue';






