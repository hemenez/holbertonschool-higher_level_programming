-- Script lists number of records with the same score in second_table
-- Script renames count as number
-- Script displays score and number
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score DESC;
