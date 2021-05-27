-- create database and table
-- table states is to be within database hbtn_0d_usa
-- states is to descrb id INT, name VARCHAR(256)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY, name VARCHAR(256) NOT NULL);