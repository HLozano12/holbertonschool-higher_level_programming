-- List cities of CA found in DB
-- states table contains one record where name=CA
-- id can be diff
-- CANNOT USE JOIN
-- ascending cities.id
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id IN (SELECT states.id, FROM states, WHERE states.name = 'California')
ORDER BY cities.id ASC;
