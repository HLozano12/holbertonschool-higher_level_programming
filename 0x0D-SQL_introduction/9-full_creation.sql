-- Create table second_table in database
-- multiple rows id, name, score
-- SELECT and SHOW not allowed
CREATE TABLE IF NOT EXIST second_table (
    id INT,
    name VARCHAR(256),
    score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10), (2, "Alex", 3), (3, "Bob", 14), (4, "George", 8);