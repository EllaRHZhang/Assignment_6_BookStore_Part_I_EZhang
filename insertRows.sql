PRAGMA foreign_keys = ON;

#category
INSERT INTO category (categoryId, categoryName, categoryImage) VALUES
(1, 'Romance', 'romance.jpg'),
(2, 'Fiction', 'fiction.jpg'),
(3, 'Biography', 'biography.jpg'),
(4, 'Science', 'science.jpg');

#romance
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(1, 1, 'Pride and Prejudice', 'Jane Austen', '9780141439518', 12.99, 'pride.jpg', 1),
(2, 1, 'Me Before You', 'Jojo Moyes', '9780143124542', 14.99, 'mebeforeyou.jpg', 0),
(3, 1, 'Twilight', 'Stephenie Meyer', '9780316015844', 13.99, 'twilight.jpg', 1),
(4, 1, 'Love in a Fallen City', 'Eileen Chang', '9780141198545', 13.99, 'fallen_city.jpg', 0);

#fiction
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(5, 2, '1984', 'George Orwell', '9780451524935', 11.99, '1984.jpg', 1),
(6, 2, 'The Great Gatsby', 'F. Scott Fitzgerald', '9780743273565', 10.99, 'gatsby.jpg', 0),
(7, 2, 'The Catcher in the Rye', 'J.D. Salinger', '9780316769488', 12.50, 'catcher.jpg', 0),
(8, 2, 'To Live', 'Yu Hua', '9781400031863', 15.99, 'tolive.jpg', 1);

#biography
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(9, 3, 'Steve Jobs', 'Walter Isaacson', '9781451648539', 18.99, 'jobs.jpg', 1),
(10, 3, 'Becoming', 'Michelle Obama', '9781524763138', 19.99, 'becoming.jpg', 1),
(11, 3, 'Elon Musk', 'Ashlee Vance', '9780062301239', 17.99, 'musk.jpg', 0);

#science
INSERT INTO book (bookId, categoryId, title, author, isbn, price, image, readNow) VALUES
(12, 4, 'A Brief History of Time', 'Stephen Hawking', '9780553380163', 15.99, 'time.jpg', 1),
(13, 4, 'The Selfish Gene', 'Richard Dawkins', '9780199291151', 14.50, 'selfishgene.jpg', 0),
(14, 4, 'Cosmos', 'Carl Sagan', '9780345539434', 16.99, 'cosmos.jpg', 1);
