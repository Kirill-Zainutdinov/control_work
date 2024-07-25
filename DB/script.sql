CREATE SCHEMA human_friends;

-- CREATE TABLE human_friends.pets (
--   idPets INT NOT NULL AUTO_INCREMENT,
--   type VARCHAR(45) NOT NULL,
--   name VARCHAR(45) NOT NULL,
--   birthday DATE NOT NULL,
--   commands MEDIUMTEXT NULL,
--   PRIMARY KEY (idPets));

-- CREATE TABLE human_friends.pack_animals (
--   idPets INT NOT NULL AUTO_INCREMENT,
--   type VARCHAR(45) NOT NULL,
--   name VARCHAR(45) NOT NULL,
--   birthday DATE NOT NULL,
--   commands MEDIUMTEXT NULL,
--   PRIMARY KEY (idPets));

CREATE TABLE human_friends.dog (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

CREATE TABLE human_friends.cat (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

CREATE TABLE human_friends.hamster (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

CREATE TABLE human_friends.horse (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

CREATE TABLE human_friends.camel (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

CREATE TABLE human_friends.donkey (
  idPets INT NOT NULL AUTO_INCREMENT,
  type VARCHAR(45) NOT NULL,
  name VARCHAR(45) NOT NULL,
  birthday DATE NOT NULL,
  commands MEDIUMTEXT NULL,
  PRIMARY KEY (idPets));

INSERT INTO human_friends.dog (type, name, birthday, commands) VALUES ('dog', 'Fido', '2021-01-01', 'Sit, Stay, Fetch');
INSERT INTO human_friends.dog (type, name, birthday, commands) VALUES ('dog', 'Buddy', '2019-12-10', 'Sit, Paw, Bark');
INSERT INTO human_friends.dog (type, name, birthday, commands) VALUES ('dog', 'Bella', '2020-11-11', 'Sit, Stay, Roll');

INSERT INTO human_friends.cat (type, name, birthday, commands) VALUES ('cat', 'Smudge', '2021-02-20', 'Sit, Pounce, Scratch');
INSERT INTO human_friends.cat (type, name, birthday, commands) VALUES ('cat', 'Oliver', '2021-06-30', 'Meow, Scratch, Jump');

INSERT INTO human_friends.hamster (type, name, birthday, commands) VALUES ('hamster', 'Hammy', '2022-03-10', 'Roll, Hide');
INSERT INTO human_friends.hamster (type, name, birthday, commands) VALUES ('hamster', 'Peanut', '2022-08-01', 'Roll, Spin');

INSERT INTO human_friends.horse (type, name, birthday, commands) VALUES ('Horse', 'Thunder', '2016-07-21', 'Trot, Canter, Gallop');
INSERT INTO human_friends.horse (type, name, birthday, commands) VALUES ('Horse', 'Storm', '2015-05-05', 'Trot, Canter');
INSERT INTO human_friends.horse (type, name, birthday, commands) VALUES ('Horse', 'Blaze', '2022-02-29', 'Trot, Jump, Gallop');

INSERT INTO human_friends.camel (type, name, birthday, commands) VALUES ('Camel', 'Sandy', '2017-11-03', 'Walk, Carry Load');
INSERT INTO human_friends.camel (type, name, birthday, commands) VALUES ('Camel', 'Dune', '2022-12-12', 'Walk, Sit');
INSERT INTO human_friends.camel (type, name, birthday, commands) VALUES ('Camel', 'Sahara', '2021-08-14', 'Walk, Run');

INSERT INTO human_friends.donkey (type, name, birthday, commands) VALUES ('Donkey', 'Eeyore', '2023-09-18', 'Walk, Carry Load, Bray');
INSERT INTO human_friends.donkey (type, name, birthday, commands) VALUES ('Donkey', 'Burro', '2020-01-23', 'Walk, Bray, Kick');

DROP TABLE human_friends.camel;

CREATE TABLE human_friends.pack_animals
SELECT * FROM human_friends.horse
UNION
SELECT * FROM human_friends.donkey;

CREATE TABLE human_friends.yong_animals
SELECT * FROM human_friends.pack_animals
WHERE DATEDIFF(CURRENT_DATE, birthday) / 365 <= 3
UNION
SELECT * FROM human_friends.dog
WHERE DATEDIFF(CURRENT_DATE, birthday) / 365 <= 3
UNION
SELECT * FROM human_friends.cat
WHERE DATEDIFF(CURRENT_DATE, birthday) / 365 <= 3
UNION
SELECT * FROM human_friends.hamster
WHERE DATEDIFF(CURRENT_DATE, birthday) / 365 <= 3
;