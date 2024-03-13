-- list all genres from hbtn_0d_tvshows and display the numbeer of shows linked to each
SHOW DISTINCT tv_genres.name AS 'genre', COUNT(tv_shows_genres.genre_id) AS 'number_of_shows' 
FROM tv_genres
LEFT JOIN tv_shows_genres
ON tv_genres.id = tv_shows_genres.genre_id
GROUP BY genre
ORDER BY number_of_shows DESC;