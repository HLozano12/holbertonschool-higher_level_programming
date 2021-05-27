-- list all cities contained in hbtn_0d_usa
-- record shold display cities.id - cities.name - states.name
-- stored in asc by cities.id
SELECT citites.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
