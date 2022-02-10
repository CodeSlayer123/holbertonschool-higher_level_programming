--  lists all shows in hbtn_0d_tvshows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_show_genres.genre_id=tv_shows.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
