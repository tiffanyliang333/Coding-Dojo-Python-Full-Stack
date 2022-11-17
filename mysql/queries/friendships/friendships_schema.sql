INSERT INTO users (id, first_name, last_name)
VALUES (1, 'Amy', 'Giver'), (2, 'Eli', 'Byers'), (3, 'Marky', 'Mark'), (4, 'Big', 'Bird'), (5, 'Kermit', 'Frog'), (6, 'Ronald', 'Macdonald');

INSERT INTO friendships (user_id, friend_id)
VALUES (1,2), (1,4), (1,6), (2,1), (2,3), (2,5), (3,2), (3,5), (4,3), (5,1), (5,6), (6,2), (6,3);

SELECT users.first_name, users.last_name, users2.first_name as friend_first_name, users2.last_name as friend_last_name FROM users
JOIN friendships ON user_id = friendships.user_id
LEFT JOIN users as user2 ON user2.id = friendships.user_id;

SELECT users2.first_name as first_name, users2.last_name as last_name, users.first_name as friends_with FROM users
JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as users2 on users2.id = friendships.friend_id 
WHERE users.id = 1;

SELECT COUNT(*) as num_of_friendships from friendships;

SELECT user_id, users.first_name, users.last_name, count(user_id) as num_of_friends from friendships
JOIN users on users.id = friendships.user_id
GROUP BY user_id
ORDER BY num_of_friends DESC
LIMIT 1;

SELECT users2.first_name as first_name, users2.last_name = last_name, users.first_name as friends_with FROM users
JOIN friendships on users.id = friendships.user_id
LEFT JOIN users as users2 ON users2.id = friendships.friend_id
WHERE users.id = 3
ORDER BY first_name;

SELECT * FROM friendships;