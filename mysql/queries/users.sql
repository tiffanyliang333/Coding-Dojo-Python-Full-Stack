INSERT INTO user (id, first_name, last_name, email, created_at, updated_at)
VALUES (1, 'Tiffany', 'Liang', 'xyz@gmail.com', NOW(), NOW()), (2, 'Sara', 'Lee', 'abc@gmail.com', NOW(), NOW()), (3, 'Dolly', 'Dog', 'dog@gmail.com', NOW(), NOW());

SELECT *
FROM user;

SELECT *
FROM user
WHERE email = 'xyz@gmail.com';

SELECT *
FROM user
WHERE id = 3;

UPDATE user
SET last_name = 'Pancakes'
WHERE id = 3;

DELETE FROM user
WHERE id = 2;

SELECT *
FROM user
ORDER BY first_name ASC;

SELECT *
FROM user
ORDER BY first_name DESC;