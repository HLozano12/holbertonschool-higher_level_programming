-- Create table id_not_null
-- descp of id INT with default value 1
-- name is VARCHAR(256)
-- if already exist, continue
CREATE TABLE IF NOT EXIST id_not_null (id INT DEFAULT 1, name VARCHAR(256));
