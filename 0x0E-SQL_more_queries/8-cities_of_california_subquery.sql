-- script lists all cities of California that can be found in database
-- results are sorted in ascending order by cities.id
SELECT cities.id, cities.name FROM cities WHERE state_id=1 ORDER BY cities.id ASC;
