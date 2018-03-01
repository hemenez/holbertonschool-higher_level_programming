-- script lists all shows contained in dumped database
-- lists genre, if none = null
-- record displays title and genre id
-- results sorted in asc order by title and id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_show_genres
RIGHT OUTER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id, tv_shows.title
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
