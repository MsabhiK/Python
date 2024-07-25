USE names_schema;
UPDATE names_schema.names SET name="Lobna CHOUCHENE"
WHERE id=3;
SELECT * FROM names;
INSERT INTO names (name, created_at, updated_at) VALUES ("Hela MSABHI", NOW(), NOW()), ("Mahbouba CHERIF", NOW(), NOW()), ("Fahima JOUINI", NOW(), NOW());
SELECT * FROM names;
DELETE FROM names 
WHERE id IN (7, 8, 9);

SELECT * FROM names;