-- import a DB dump from hbtn_0d_tvshows to download server
-- list all shows contained in hbtn_0d_tvshows with at least one link genre
-- sort in ASC by tv_shows.title & tv_show_genre.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
RIGHT JOIN tv_shows_genres
ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
