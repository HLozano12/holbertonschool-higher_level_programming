-- list the number of records with same score in the table second_table
-- display score, number of records of score w/ number
-- Descending order
SELECT score, count(score) as number
        FROM second_table
        GROUP BY score
        ORDER BY score DESC;
