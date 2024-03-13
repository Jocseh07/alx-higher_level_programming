-- List of al genres of show Dexter
SELECT name
FROM tv_genres
LEFT JOIN tv_shows_genres
ON tv_genres.id = tv_shows_genres.genre_id
LEFT JOIN tv_shows
ON tv.tv_shows_genres.show_id = tv_shows.id
WHERE tv_shows.title = 'Dexter'
GROUP BY name
ORDER BY name;