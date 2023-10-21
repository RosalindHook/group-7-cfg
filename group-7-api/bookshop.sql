-- BOOKSHOP DATABASE
-- This SQL script sets up a bookshop database for a new shop, "Seventh Heaven", with four separate branches all owned and run by the Code Queens.
-- It currently includes the following tables: authors, genres, books (incl prices), store branches, store owners and availability of stock in each branch.
-- The script below sets up these tables and then populates them with mock data.

-- Creates Bookshop Database
DROP DATABASE IF EXISTS seventhHeaven;
CREATE DATABASE seventhHeaven;
USE seventhHeaven;

-- Genres Table: To store info about genres of the books
CREATE TABLE genres (
  GenreID INT,
  GenreName VARCHAR(50) NOT NULL
);

-- Author table: stores info about book authors
CREATE TABLE authors (
	AuthorID INT,
    FirstName VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL
);

-- Books Table: To store info about book stock and prices
CREATE TABLE books (
    BookID SERIAL PRIMARY KEY,
    Title VARCHAR(250) NOT NULL,
    AuthorID INT REFERENCES authors(AuthorID),  -- FK relationship
    GenreID INT REFERENCES genres(GenreID),   -- FK relationship
    Price FLOAT
);

-- Store branch table: To store info about store branches
CREATE TABLE storeBranch (
	BranchID SERIAL PRIMARY KEY,
    Location VARCHAR(250) NOT NULL
);

-- Store owner table: To store info about the Code Queens
CREATE TABLE storeOwner (
	OwnerID SERIAL PRIMARY KEY,
    OwnerName VARCHAR(250) NOT NULL,
    LocationID INT REFERENCES storeBranch(Location)   -- FK relationship
);

CREATE TABLE bookAvailability (
    AvailabilityID SERIAL PRIMARY KEY,
    BookID INT REFERENCES books(BookID), -- FK to the books table
    BranchID INT REFERENCES storeBranch(BranchID), -- FK to the storeBranch table
    Availability BOOLEAN,
    Stock INT
);

-- Populating tables with data
-- Adding data into the Genres table
INSERT INTO Genres (GenreID, GenreName)
VALUES
  (301, 'Fantasy'),
  (401, 'Non-Fiction'),
  (501, 'Science Fiction'),
  (601, 'Crime'),
  (701, 'Romance'),
  (801, 'Childrens'),
  (901, 'Self-Help');
  
-- Adding data into the Authors table
INSERT INTO Authors 
  (AuthorID, FirstName, Surname)
VALUES
    (1, 'J.K.', 'Rowling'),  
    (2, 'J.R.R.', 'Tolkien'), 
    (3, 'Frank', 'Herbert'),  
    (4, 'James', 'Clear'),  
    (5, 'Agatha', 'Christie'),  
    (6, 'Roald', 'Dahl'),  
    (7, 'Jane', 'Austen'),  
    (8, 'Yuval', 'Harari');   
    
-- Adding data into the Books table
INSERT INTO Books (Title, AuthorID, GenreID, Price)
VALUES
    ('Harry Potter and the Chamber of Secrets', 1, 301, 10.00),
    ('The Lord of the Rings', 2, 301, 6.99),
    ('Dune', 3, 501, 5.99),
    ('Atomic Habits', 4, 901, 4.99),
    ('Death on the Nile', 5, 601, 6.99),
    ('Charlie and the Chocolate Factory', 6, 801, 8.99),  
    ('Pride and Prejudice', 7, 701, 2.99),
    ('Homo Deus', 8, 401, 12.50),
    ('The Hobbit', 2, 301, 7.50),
    ('Harry Potter and the Prisoner of Azkaban', 1, 401, 10.00);

-- Adding data into the branch table
INSERT INTO storeBranch (Location)
VALUES
	('Sutton'),
    ('Glasgow'),
    ('London'),
    ('Edinburgh');

-- Adding data into store owner table
INSERT INTO storeOwner (OwnerName, LocationID)
VALUES
	('Ros', 1),
    ('Rebecca', 2),
    ('Sriya', 3),
    ('Olga', 4);
    
-- Adding data to book availability
INSERT INTO bookAvailability (BookID, BranchID, Availability, Stock)
VALUES
    (1, 1, true, 25),
    (2, 1, false, 0),
    (3, 1, false, 0),
    (4, 1, true, 10),
    (5, 1, true, 5),
    (6, 1, true, 8),
    (7, 1, true, 20),
    (8, 1, false, 0),
    (9, 1, true, 40),
    (10, 1, true, 10),

    (1, 2, true, 20),
    (2, 2, true, 10),
    (3, 2, true, 5),
    (4, 2, true, 15),
    (5, 2, true, 10),
    (6, 2, true, 12),
    (7, 2, true, 18),
    (8, 2, true, 25),
    (9, 2, true, 35),
    (10, 2, false, 0),

    (1, 3, true, 30),
    (2, 3, false, 0),
    (3, 3, true, 18),
    (4, 3, true, 27),
    (5, 3, true, 23),
    (6, 3, true, 30),
    (7, 3, true, 28),
    (8, 3, true, 40),
    (9, 3, true, 45),
    (10, 3, false, 0),

    (1, 4, true, 25),
    (2, 4, true, 20),
    (3, 4, false, 0),
    (4, 4, true, 18),
    (5, 4, true, 20),
    (6, 4, true, 22),
    (7, 4, true, 23),
    (8, 4, true, 30),
    (9, 4, true, 35),
    (10, 4, false, 10);

-- This stored procedure retrieves the availability and price of a book at different store branches based on the book title.

DELIMITER //
CREATE PROCEDURE FindBookAvailability(IN bookTitle VARCHAR(250))
BEGIN
  SELECT
    b.Title AS BookTitle,
    sb.Location AS StoreBranch,
    ba.Availability AS IsAvailable,
    b.Price AS BookPrice
  FROM books AS b
  JOIN bookAvailability AS ba ON b.BookID = ba.BookID
  JOIN storeBranch AS sb ON ba.BranchID = sb.BranchID
  WHERE b.Title = bookTitle;
END; 

CALL FindBookAvailability('Harry Potter and the Prisoner of Azkaban');

-- This stored procedure retrieves all available books in a specific branch
DELIMITER //
CREATE PROCEDURE GetBooksInBranch(IN branchName VARCHAR(250))
BEGIN
  SELECT
    b.BookID,
    b.Title,
    a.FirstName,
    a.Surname AS Author,
    g.GenreName AS Genre,
    ba.Price AS Price
  FROM books AS b
  JOIN authors AS a ON b.AuthorID = a.AuthorID
  JOIN genres AS g ON b.GenreID = g.GenreID
  JOIN bookAvailability AS ba ON b.BookID = ba.BookID
  JOIN storeBranch AS sb ON ba.BranchID = sb.BranchID
  WHERE sb.Location = branchName AND ba.Availability = TRUE;
END;



