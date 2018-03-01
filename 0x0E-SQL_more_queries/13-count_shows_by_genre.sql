-- script lists all genres and displays number of shows linked
-- doesn't display a genre that has no shows linked
-- record displays genre title and number of shows
-- results sorted in desc order by number of shows linked
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id)
AS 'number_shows'
FROM tv_show_genres
INNER JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.id
ORDER BY COUNT(tv_show_genres.genre_id) DESC;
