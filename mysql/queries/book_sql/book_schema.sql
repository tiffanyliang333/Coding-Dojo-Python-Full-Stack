-- INSERT INTO users(id, first_name, last_name)
-- VALUES (1, 'Jane', 'Amsden'), (2, 'Emily', 'Dixon'), (3, 'Theodore', 'Dostoevsky'), (4, 'William', 'Shapiro'), (5, 'Lao', 'Xiu');

-- INSERT INTO books(id, title)
-- VALUES (1, 'C Sharp'), (2, 'Java'), (3, 'Python'), (4, 'PHP'), (5, 'Ruby');

-- UPDATE books
-- SET title = 'C#'
-- WHERE id = 1;

-- UPDATE users
-- SET first_name = 'Bill'
-- WHERE id = 4;

-- INSERT INTO favorites (user_id, book_id)
-- VALUES (1,1);

-- INSERT INTO favorites (user_id, book_id)
-- VALUES (2,1), (2,2), (2,3);

-- INSERT INTO favorites (user_id, book_id)
-- VALUES (3,1), (3,2), (3,3), (3,4);

-- INSERT INTO favorites (user_id, book_id)
-- VALUES (4,1), (4,2), (4,3), (4,4), (4,5);

-- SELECT id, first_name, last_name FROM users
-- JOIN favorites ON users.id = favorites.user_id
-- WHERE favorites.book_id = 3;

-- DELETE FROM favorites
-- WHERE user_id = 2 AND book_id = 3;

-- INSERT INTO favorites (user_id, book_id)
-- VALUES (5,2);

-- SELECT * FROM favorites
-- JOIN favorites on book_id = favorites.book_id
-- WHERE favorites.user_id = 3;

-- SELECT * from users
-- JOIN favorites on favorites.user_id = users.id
-- WHERE favorites.book_id = 5;

SELECT *
FROM users;

SELECT *
FROM books;

SELECT *
FROM favorites;