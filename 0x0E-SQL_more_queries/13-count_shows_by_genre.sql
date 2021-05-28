-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- You can use only one SELECT statement
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
