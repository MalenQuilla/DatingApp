DROP database IF EXISTS DatingApp;
CREATE database IF NOT EXISTS DatingApp;
USE DatingApp;

CREATE TABLE User_information (
User_name TEXT DEFAULT NULL,
User_age INT DEFAULT NULL,
User_gender TEXT DEFAULT NULL,
User_location TEXT DEFAULT NULL,
User_bio TEXT DEFAULT NULL,
Status TEXT DEFAULT NULL
);

CREATE TABLE User_account (
Account_username TEXT DEFAULT NULL,
Account_password TEXT DEFAULT NULL,
Status TEXT DEFAULT NULL
);

CREATE TABLE User_basics (
Basics_height TEXT DEFAULT NULL,
Basics_weigth TEXT DEFAULT NULL,
Basics_zodiac TEXT DEFAULT NULL,
Basics_education TEXT DEFAULT NULL,
Basics_workout TEXT DEFAULT NULL,
Basics_smoke TEXT DEFAULT NULL,
Basics_drink TEXT DEFAULT NULL,
Status TEXT DEFAULT NULL
);

CREATE TABLE User_interests (
Interests_sports TEXT DEFAULT NULL,
Interests_creativity TEXT DEFAULT NULL,
Interests_goingout TEXT DEFAULT NULL,
Interests_stayingin TEXT DEFAULT NULL,
Interests_film_tv TEXT DEFAULT NULL,
Interests_reading TEXT DEFAULT NULL,
Interests_music TEXT DEFAULT NULL,
Interests_food TEXT DEFAULT NULL,
Interests_travelling TEXT DEFAULT NULL,
Interests_pet TEXT DEFAULT NULL,
Status TEXT DEFAULT NULL
);

DELIMITER $$
CREATE PROCEDURE New_User
(IN User_name VARCHAR(100), IN User_age INT, IN User_gender VARCHAR(100), IN User_location VARCHAR(100),
IN User_bio VARCHAR(100))
BEGIN
INSERT INTO User_information (User_name, User_age, User_gender, User_location, User_bio)
VALUES (User_name, User_age, User_gender, User_location, User_bio) ;
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE New_Account
(IN User_account_username VARCHAR(100), IN User_account_password VARCHAR(100))
BEGIN
INSERT INTO User_account (User_account_username, User_account_password)
VALUES (User_account_username, User_account_password);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE Basics
(IN User_basics_height VARCHAR(100), IN User_basics_weight VARCHAR(100), IN User_basics_zodiac VARCHAR(100),
IN User_basics_education VARCHAR(100), IN User_basics_workout VARCHAR(100), IN User_basics_smoke VARCHAR(100),
IN User_basics_drink VARCHAR(100))
BEGIN
INSERT INTO User_basics (User_basics_height, User_basics_weight, User_basics_zodiac, User_basics_education,
User_basics_workout, User_basics_smoke, User_basics_drink)
VALUES (User_basics_height, User_basics_weight, User_basics_zodiac, User_basics_education,
User_basics_workout, User_basics_smoke, User_basics_drink);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE Interests
(IN User_interests_sports VARCHAR(100), IN User_interests_creativity VARCHAR(100),
IN User_interests_goingout VARCHAR(100), IN User_interests_stayingin VARCHAR(100), IN User_interests_film_tv VARCHAR(100),
IN User_interests_reading VARCHAR(100), IN User_interests_music VARCHAR(100), IN User_interests_food VARCHAR(100),
IN User_interests_travelling VARCHAR(100), IN User_interests_pets VARCHAR(100))
BEGIN
INSERT INTO User_interests (User_interests_sports, User_interests_creativity, User_interests_goingout, 
User_interests_stayingin, User_interests_film_tv, User_interests_reading, User_interests_music, User_interests_food,
User_interests_travelling, User_interests_pets)
VALUES (User_interests_sports, User_interests_creativity, User_interests_goingout, 
User_interests_stayingin, User_interests_film_tv, User_interests_reading, User_interests_music, User_interests_food,
User_interests_travelling, User_interests_pets);
END $$
DELIMITER ; 

Call New_Account ('anhtung207', 'Pass123');
 