-- list shows and all genres linked to that show
SELECT title, name
FROM tv_shows
LEFT JOIN tv_shows_genres
ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres
ON tv_shows_genres.genre_id = tv_genres.id
ORDER BY title, name;