-- lists all shows in database hbtn_0d_tvshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM hbtn_0d_tvshows
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;