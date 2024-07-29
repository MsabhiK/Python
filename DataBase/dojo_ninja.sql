USE dojo_ninja;
	/*Query: Create 3 new dojos*/
/*INSERT INTO dojos (name) VALUES ('KASSERINE'), ('SIDI BOUZID'), ('EL KEF');*/
	/*Query: Delete the 3 dojos you just created*/
/*DELETE FROM dojos WHERE id IN (8, 9, 10);*/
	/*Query: Create 3 more dojos*/
/*INSERT INTO dojos (name) VALUES ('HAMMAMET'), ('KEBILI'), ('EL BORMA');
SELECT * FROM dojos;*/

	/*Query: Create 3 ninjas that belong to the first dojo*/
/*INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (1, 'Mourad', 'Feddaoui', 42), (1, 'Nacer', 'BEN_ZINE', 41), (1, 'Salma', 'CHAOUACHI', 32);
SELECT * FROM ninjas;*/

	/*Query: Create 3 ninjas that belong to the second dojo*/
/*INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (2, 'Zied', 'Gannouni', 47), (2, 'Ameur', 'BRAHAM', 43), (2, 'Islem', 'CHAOUACHI', 39);
SELECT * FROM ninjas;*/

	/*Query: Create 3 ninjas that belong to the third dojo*/
/*INSERT INTO ninjas (dojo_id, first_name, last_name, age) 
VALUES (3, 'Yousra', 'Khouja', 51), (3, 'Ala', 'Zneydi', 46), (3, 'Mtir', 'Ben Hsin', 41);
SELECT * FROM ninjas;*/

	/*Query: Retrieve all the ninjas from the first dojo*/
/*select * from ninjas where dojo_id=1;*/
	/*Query: Retrieve all the ninjas from the last dojo*/
/*select * from ninjas where dojo_id=13;*/
	/*Query: Retrieve the last ninja's dojo*/
/*select dojo_id from ninjas where id=16;*/

/*Query: Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo. Be sure to do this in one query using a join statement.*/
/*SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id where ninjas.id=6;*/

/*Query: Use a JOIN to retrieve all the ninjas as well as that ninja's dojo, note, you will see repeated data on dojos as a dojo can have many ninjas!*/
SELECT * FROM ninjas 
JOIN dojos ON dojos.id = ninjas.dojo_id;
