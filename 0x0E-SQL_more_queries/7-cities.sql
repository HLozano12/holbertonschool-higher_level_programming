-- create db hbtn_0d_usa with table cities in it
-- id INT, auto generate not NULL
-- state_id INT, not NULL and must be FOREIGN KEY
-- Foreign key must reference ID of STATES talbe
-- name is still VARCHAR(256) and not NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY NOT NULL, state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
    