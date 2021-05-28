-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

