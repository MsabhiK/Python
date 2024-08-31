SELECT * FROM users_cr.users;
INSERT INTO users (classroom_id, first_name, last_name, email) VALUE (1, "Karim", "MSABHI", "sirmsabhi@gmail.com"); 
SELECT * FROM users_cr.users;
INSERT INTO users (classroom_id, first_name, last_name, email) VALUE (1, "Lobna", "CHOUCHANE", "lobna.chouchenei@gmail.com"), (3, "Hela", "MSABHI", "helaMsabhi@gmail.com"); 
SELECT * FROM users_cr.users;
SELECT * FROM users LEFT JOIN classrooms ON users.classroom_id = classrooms.id;
INSERT INTO users (first_name, last_name, email, classroom_id) VALUE ("Hiba", "HMILA", "hiba.hmila@gmail.com", 2);