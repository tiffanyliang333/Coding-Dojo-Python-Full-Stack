-- INSERT INTO dojos(id, name)
-- VALUES (1, 'Dojo1'), (2, 'Dojo2'), (3, 'Dojo3');

-- SET SQL_SAFE_UPDATES = 0;
-- DELETE FROM dojos;

-- INSERT INTO dojos(id, name)
-- VALUES (1, 'Dojo1'), (2, 'Dojo2'), (3, 'Dojo3');

-- SELECT *
-- FROM dojos;

-- INSERT INTO ninjas (id, dojo_id, first_name, last_name, age)
-- VALUES (1, 1, 'Dolly', 'Dog', 11), (2, 1, 'Yuki', 'Cat', 4), (3, 1, 'Okami', 'Dog', 7);

-- INSERT INTO ninjas (id, dojo_id, first_name, last_name, age)
-- VALUES (4, 2, 'Piggy', 'Pig', 20), (5, 2, 'Kuro', 'Rabbit', 5), (6, 2, 'Neko', 'Cat', 5);

-- INSERT INTO ninjas (id, dojo_id, first_name, last_name, age)
-- VALUES (7, 3, 'Zyra', 'Whispers', 21), (8, 3, 'Xayah', 'Ragewing', 25), (9, 3, 'Yone', 'Mirage', 30);

-- SELECT *
-- FROM dojos
-- LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
-- WHERE dojo_id = 1;

-- SELECT *
-- FROM dojos
-- LEFT JOIN ninjas on dojos.id = ninjas.dojo_id
-- WHERE dojo_id = 3;

-- SELECT *
-- FROM dojos
-- WHERE dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC)