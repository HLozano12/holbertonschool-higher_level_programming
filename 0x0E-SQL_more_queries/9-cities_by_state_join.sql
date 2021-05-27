-- list all cities contained in hbtn_0d_usa
-- record shold display cities.id - cities.name - states.name
-- stored in asc by cities.id
SELECT cities.id AS id,  cities.name AS name, states.name AS name
FROM cities INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
