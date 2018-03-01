-- Script uses database to list all genres of Dexter
-- Record displays genre name
-- Results in ASC order by genre name
SELECT tv_genres.name
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.show_id = 8
GROUP BY tv_genres.id
ORDER BY tv_genres.name ASC;
