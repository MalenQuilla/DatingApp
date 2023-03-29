DROP database IF EXISTS DatingApp;
CREATE database IF NOT EXISTS DatingApp;
USE DatingApp;

CREATE TABLE User_information (
User_name TEXT DEFAULT NULL,
User_dob TEXT DEFAULT NULL,
User_gender TEXT DEFAULT NULL,
User_location TEXT DEFAULT NULL,
User_bio TEXT DEFAULT NULL
);

CREATE TABLE User_account (
Account_username TEXT DEFAULT NULL,
Account_password TEXT DEFAULT NULL
);

CREATE TABLE User_basics (
Basics_height TEXT DEFAULT NULL,
Basics_weight TEXT DEFAULT NULL,
Basics_zodiac TEXT DEFAULT NULL,
Basics_education TEXT DEFAULT NULL,
Basics_workout TEXT DEFAULT NULL,
Basics_smoke TEXT DEFAULT NULL,
Basics_drink TEXT DEFAULT NULL
);

CREATE TABLE User_interests (
interest1 TEXT DEFAULT NULL,
interest2 TEXT DEFAULT NULL,
interest3 TEXT DEFAULT NULL,
interest4 TEXT DEFAULT NULL,
interest5 TEXT DEFAULT NULL
);

CREATE TABLE User_photo (
image LONGBLOB NOT NULL
);