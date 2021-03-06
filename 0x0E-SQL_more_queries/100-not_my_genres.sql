-- not my genres

SELECT name FROM tv_genres WHERE tv_genres.id not in(
    SELECT tv_show_genres.genre_id FROM tv_shows
    JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id WHERE tv_shows.title = 'Dexter'
    )
    ORDER BY tv_genres.name;