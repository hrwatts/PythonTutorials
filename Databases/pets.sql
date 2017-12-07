# A simple starter database if you've just installed MySQL on your device and have no DBs to use.
# This is on MySQLs website for tutorials
# https://dev.mysql.com/doc/mysql-getting-started/en/
# you can do this through MySQL in terminal by running this script
# use source pets.sql

DROP DATABASE IF EXISTS pets;
CREATE DATABASE pets;

USE pets;

CREATE TABLE cats
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the cat
  owner           VARCHAR(150) NOT NULL,                # Owner of the cat
  birth           DATE NOT NULL,                        # Birthday of the cat
  PRIMARY KEY     (id)                                  # Make the id the primary key
);

#add some cats
INSERT INTO cats ( name, owner, birth) VALUES
  ( 'Whiskers', 'Brandon', '2015-01-03' ),
  ( 'Socks', 'Casey', '2013-11-13' ),
  ( 'Snow Ball', 'Jacob', '2016-05-21' );

CREATE TABLE dogs
(
  id              INT unsigned NOT NULL AUTO_INCREMENT, # Unique ID for the record
  name            VARCHAR(150) NOT NULL,                # Name of the dog
  owner           VARCHAR(150) NOT NULL,                # Owner of the dog
  birth           DATE NOT NULL,                        # Birthday of the dog
  breed		  VARCHAR(50),				# Breed of dog optional
  PRIMARY KEY     (id)                                  # Make the id the primary key
);

#add some dogs
INSERT INTO dogs ( name, owner, birth, breed) VALUES
  ( 'Spot', 'Brandon', '2005-11-22', 'Poodle' ),
  ( 'Sir Bark', 'Kyle', '2010-12-03', 'Corgi' ),
  ( 'Peaches', 'Kim', '2013-06-14', 'Husky' );

