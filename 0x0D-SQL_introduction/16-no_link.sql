-- list all records of second_table
-- don't list row w/o name value
-- display in order of score and name
-- desc order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
